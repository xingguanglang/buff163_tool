from item import buff_item,market_url,item
from utils_storage import write_buff_item_to_json,read_buff_item_from_json
from playwright.sync_api import sync_playwright,TimeoutError
from time import time,sleep
rarity_list = [("ancient_weapon","隐蔽"),("legendary_weapon","保密"),("mythical_weapon","受限"),("rare_weapon","军规级"),("uncommon_weapon","工业级"),("common_weapon","消费级")]
rarity_list= [("ancient_weapon","隐蔽"),("legendary_weapon","保密"),("mythical_weapon","受限"),("rare_weapon","军规级")]

quality_list = [("normal","普通")]

exterior_list = [("wearcategory0","崭新出厂"),("wearcategory1","略有磨损"),("wearcategory2","久经沙场"),("wearcategory3","破损不堪"),("wearcategory4","战痕累累"),]
exterior_list = [("wearcategory0","崭新出厂"),("wearcategory1","略有磨损"),("wearcategory2","久经沙场")]

itemset_list = [("set_community_33","千瓦"),("set_community_30","梦魇"),]
itemset_list = [("set_community_30","梦魇")]

sleeptime = 0

def generate_market_url():
    url = []
    for i in rarity_list:
        for j in quality_list:
            for k in exterior_list:
                for x in itemset_list:
                    url.append(market_url(i,j,k,x))
    return url

def generate_buff_item_list_from_market_url(market_url:market_url):
    usr_data_dir = "browser_buffer/chrome"
    selector = "#j_list_card > ul > li"

    result = []
    with sync_playwright() as p:
        start = time()
        browser = p.chromium.launch_persistent_context(usr_data_dir, headless=True)
        page = browser.new_page()
        page.goto(url=market_url.url)
        try:
            page.wait_for_selector(selector,timeout=3000)
        except(TimeoutError):
            sleep(sleeptime)
            page.reload()
            try:
                page.wait_for_selector(selector,timeout=3000)
            except(TimeoutError):
                print(f"找不到元素: 收藏品:{market_url.itemset[1]}, 等级:{market_url.quality[1]}, 外观:{market_url.exterior[1]}, 磨损:{market_url.rarity[1]}, 花费时间:{time()-start}s")
                print(f"url: {market_url.url}")
                return 1
        else:
            print(f"找到元素: 收藏品:{market_url.itemset[1]}, 等级:{market_url.quality[1]}, 外观:{market_url.exterior[1]}, 磨损:{market_url.rarity[1]}")
        value = page.locator(selector).all()
        for i in value:
            a = i.locator("h3>a").get_attribute("href")
            b = i.locator("h3>a").get_attribute("title").split("(")[0]
            a = a.split("/")[2].split("?")[0]
            print(f"编号:{a}, 名称:{b}")
            tmp = buff_item(name=b,buff_id=a,rarity=market_url.rarity[1],itemset=market_url.itemset[1],exterior=market_url.exterior[1])
            result.append(tmp)
        # page.wait_for_timeout(99999999)
        print(f"花费时间{time()-start}s")
    return result

def create_buff_item_main():
    market_url_list = generate_market_url()
    result = []
    for i in market_url_list:
        
        tmp = generate_buff_item_list_from_market_url(i)
        if tmp!=1:
            for j in tmp:
                result.append(j)
    write_buff_item_to_json(buff_items=result)
    return

if __name__ == "__main__":
    market_url_list = generate_market_url()
    result = []
    count = 0
    for i in market_url_list:
        tmp = generate_buff_item_list_from_market_url(i)
        if tmp!=1:
            for j in tmp:
                result.append(j)
        count = count + 1
        print(f"已经完成:{count}, 总数量:{len(market_url_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(market_url_list))}")
        sleep(sleeptime)
    write_buff_item_to_json(buff_items=result)
    print("created buff_item")