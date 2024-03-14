from item import buff_item,market_url
from utils_storage import write_buff_item_to_json
from playwright.sync_api import sync_playwright,TimeoutError
from time import time,sleep

# rarity_list = [("ancient_weapon","隐蔽"),("legendary_weapon","保密"),("mythical_weapon","受限"),("rare_weapon","军规级"),("uncommon_weapon","工业级"),("common_weapon","消费级")]
rarity_list = [("ancient_weapon","隐蔽"),("legendary_weapon","保密"),("mythical_weapon","受限")]
quality_list = [("normal","普通")]

# exterior_list = [("wearcategory0","崭新出厂"),("wearcategory1","略有磨损"),("wearcategory2","久经沙场"),("wearcategory3","破损不堪"),("wearcategory4","战痕累累"),]
exterior_list = [("wearcategory0","崭新出厂"),("wearcategory1","略有磨损"),("wearcategory2","久经沙场")]
itemset_list = [("set_community_33","千瓦"),("set_community_32","变革"),
                ("set_community_31","反冲"),("set_community_30","梦魇"),
                ("set_community_29","激流大行动"),("set_community_28","蛇噬"),
                ("set_community_27","狂牙大行动"),("set_community_26","裂空"),
                ("set_community_25","棱彩2号"),("set_community_24","裂网大行动"),
                ("set_community_23","反恐精英20周年"),("set_community_22","棱彩"),
                ("set_community_21","头号特训"),("set_community_20","地平线"),
                ("set_community_19","命悬一线"),("set_community_18","光谱2号"),
                ("set_community_17","九头蛇大行动"),("set_community_16","光谱"),
                ("set_community_15","手套武器箱"),("set_community_14","伽马2号"),
                ("set_community_13","伽马"),("set_community_12","幻彩3号"),
                ("set_community_11","野火大行动"),("set_community_10","左轮武器箱"),
                ("set_community_9","暗影"),("set_community_8","弯曲猎手"),
                ("set_community_7","幻彩2号"),("set_community_6","幻彩"),
                ("set_community_5","先锋"),("set_community_4","突围"),
                ("set_community_3","猎杀者"),("set_community_2","凤凰"),
                ("set_community_1","冬季攻势"),
                ("set_esports","电竞2013"),("set_esports_ii","电竞2013冬季"),("set_esports_iii","电竞2014夏季"),
                ("set_weapons_i","反恐精英武器箱"),("set_weapons_ii","反恐精英2号武器箱"),("set_weapons_iii","反恐精英3号武器箱"),
                ("set_bravo_i","英勇武器箱")
                ]
# itemset_list = [("set_community_33","千瓦")]
# itemset_list [("set_anubis","阿努比斯"),("set_vertigo_2021","2021殒命大厦"),("set_mirage_2021","2021荒漠迷城"),
#               ("set_dust_2_2021","2021炽热沙城"),("set_train_2021","2021列车停放站"),("set_ancient","远古遗迹"),
#               ("set_op10_ct","控制收藏品"),("set_op10_t","浩劫收藏品"),("set_norse","挪威人收藏品"),
#               ("set_canals","运河水城"),("set_stmarc","圣马克镇"),("set_inferno_2","2018炼狱小镇"),
#               ("set_nuke_2","2018核子危机"),("set_gods_and_monsters","神魔收藏品"),("set_chopshop","解体厂收藏品"),
#               ("set_kimono","旭日收藏品"),("set_cache","死城之谜"),("set_overpass","死亡游乐园"),
#               ("set_cobblestone","古堡激战"),("set_baggage","行李仓库"),("set_bank","金库危机"),
#               ("set_dust_2","炽热沙城2"),("set_train","列车停放站"),("set_mirage","荒漠迷城"),
#               ("set_italy","意大利小镇"),("set_lake","湖畔激战"),("set_safehouse","安全处所"),
#               ("set_bravo_ii","无畏收藏品"),("set_dust","炽热沙城"),("set_aztec","雨林遗迹"),
#               ("set_vertigo","殒命大厦"),("set_inferno","炼狱小镇"),("set_militia","佣兵训练营"),
#               ("set_nuke","核子危机"),("set_office","办公室"),("set_assault","仓库突击"),
#               ]

sleeptime = 1

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
        try:
            print(f"url: {market_url.url}")
            page.goto(market_url.url)
            page.wait_for_selector(selector,timeout=3000)
        except(TimeoutError):
            times = 3
            while(True):
                sleep(sleeptime)
                page.reload()
                try:
                    page.wait_for_selector(selector,timeout=3000)
                except(TimeoutError):
                    print(f"找不到元素: 次数:{times}, 收藏品:{market_url.itemset[1]}, 等级:{market_url.quality[1]}, 外观:{market_url.exterior[1]}, 磨损:{market_url.rarity[1]}, 花费时间:{time()-start}s")
                    if times == 0:
                        return 1
                    times = times - 1
                else:
                    break
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
    count = 0
    for i in market_url_list:
        tmp = generate_buff_item_list_from_market_url(i)
        if tmp!=1:
            for j in tmp:
                result.append(j)
        count = count + 1
        print(f"已经完成:{count} buff items, 总数量:{len(market_url_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(market_url_list))}")
        sleep(sleeptime)
    write_buff_item_to_json(buff_items=result)
    return result
