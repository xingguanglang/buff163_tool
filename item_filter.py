from playwright.sync_api import sync_playwright,TimeoutError
from utils_storage import read_item_from_json, write_item_to_json,read_buff_item_from_json
from utils_operation import remove_redundancy
from item import item,buff_item,deep_partition
from find_url import generate_goods_url,generate_goods_url_list
from datetime import datetime
from time import time,sleep

filepath = "json/storage.json"
sleeptime=1
def generate_item_list_from_buff_item(buff_item:buff_item, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    url = generate_goods_url(buff_item)
    print("url:",url)
    with sync_playwright() as p:
        start = time()
        browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
        page = browser.new_page()
        page.goto(url)
        result = []
        try:
            page.wait_for_selector(selector,timeout=2500)
        except(TimeoutError):
            sleep(sleeptime)
            page.reload()
            try:
                page.wait_for_selector(selector,timeout=2500)
            except(TimeoutError):
                print(f"找不到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}, 花费时间:{time()-start}s")
                return 1
        value = page.locator(selector).all()
        
        print(f"找到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}")
        for i in value:
            a = i.locator("td:nth-child(3) > div > div.csgo_value > div.wear-value").inner_text().split(" ")[1]
            b = i.locator(" td:nth-child(5) > div:nth-child(1) > strong").inner_text().split(" ")[1]
            c = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
            print(f"价格:{b}, 磨损:{a}")
            tmp = item(buff_item.name,float(a),float(b),c)
            result.append(tmp)
        print(f"花费时间:{time()-start}s")
    return result

def generate_item_list_from_deep_partition(deep_partition:deep_partition, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    urls = generate_goods_url_list(deep_partition=deep_partition)
    print(urls)
    buff_item = deep_partition #懒得改变量了
    with sync_playwright() as p:
        for x in urls:
            print("url:",x)
            start = time()
            browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
            page = browser.new_page()
            page.goto(x)
            result = []
            try:
                page.wait_for_selector(selector,timeout=2500)
            except(TimeoutError):
                sleep(sleeptime)
                page.reload()
                try:
                    page.wait_for_selector(selector,timeout=2500)
                except(TimeoutError):
                    print(f"找不到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}, 花费时间:{time()-start}s")
                    return 1
            value = page.locator(selector).all()
            
            print(f"找到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}")
            for i in value:
                a = i.locator("td:nth-child(3) > div > div.csgo_value > div.wear-value").inner_text().split(" ")[1]
                b = i.locator(" td:nth-child(5) > div:nth-child(1) > strong").inner_text().split(" ")[1]
                c = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
                print(f"价格:{b}, 磨损:{a}")
                tmp = item(buff_item.name,float(a),float(b),c)
                result.append(tmp)
            print(f"花费时间:{time()-start}s")
    return result


if __name__ == '__main__':
    # generate_item_list_from_buff_item_list(buff_item(name="M4A1 消音型 | 黑莲花 (略有磨损)", exterior="略有磨损", buff_id="956471", itemset="千瓦", rarity="军规级"))
    value = []
    buff_item_list = read_buff_item_from_json()
    count = 0 
    for i in buff_item_list:
        tmp = generate_item_list_from_buff_item(i)
        if tmp !=1:
            for j in tmp:
                value.append(j)
        count = count + 1
        print(f"已经完成:{count}, 总数量:{len(buff_item_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(buff_item_list))}")
        sleep(sleeptime)
    # loads = read_item_from_json(filepath)
    # result = remove_redundancy(value,loads)
    filepath = filepath+datetime.now().strftime("%Y-%m-%d,%H:%M:%S")+".json"
    write_item_to_json(value,filepath)
    print("finish")
    #generate item with price