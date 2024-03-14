from playwright.sync_api import sync_playwright,TimeoutError
from utils_storage import  write_item_to_json
from item import item,buff_item,deep_partition
from find_url import generate_goods_url,generate_goods_url_list
from datetime import datetime
from time import time,sleep

sleeptime = 1

def generate_item_list_from_buff_item(buff_item:buff_item, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    url = generate_goods_url(buff_item)
    print("url:",url)
    with sync_playwright() as p:
        start = time()
        browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
        page = browser.new_page()
        result = []
        try: 
            page.goto(url)
        except(TimeoutError):
            return result
        
        try:
            page.wait_for_selector(selector,timeout=2500)
        except(TimeoutError):
            times = 3
            while (True):
                sleep(sleeptime)
                page.reload()
                try:
                    page.wait_for_selector(selector,timeout=2500)
                except(TimeoutError):
                    print(f"找不到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}, 花费时间:{time()-start}s")
                    if times == 0 :
                        return 1
                    times = times - 1
                else:
                    break
        value = page.locator(selector).all()
        
        print(f"找到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}")
        for y in range(len(value)):
            i = value[y]
            if y <3:
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
    buff_item = deep_partition #懒得改变量了
    with sync_playwright() as p:
        result = []
        for x in urls:
            print("url:",x)
            start = time()
            browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
            page = browser.new_page()
            try :
                page.goto(x)
            except(TimeoutError):
                continue
            try:
                page.wait_for_selector(selector,timeout=2500)
            except(TimeoutError):
                times = 3
                while (True):
                    sleep(sleeptime)
                    page.reload()
                    try:
                        page.wait_for_selector(selector,timeout=2500)
                    except(TimeoutError):
                        print(f"找不到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}, 花费时间:{time()-start}s")
                        if times == 0:
                            return 1
                        times = times - 1
                    else:
                        break
            value = page.locator(selector).all()
            
            print(f"找到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}")
            for y in range(len(value)):
                i = value[y]
                if y <3:
                    a = i.locator("td:nth-child(3) > div > div.csgo_value > div.wear-value").inner_text().split(" ")[1]
                    b = i.locator(" td:nth-child(5) > div:nth-child(1) > strong").inner_text().split(" ")[1]
                    c = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
                    print(f"价格:{b}, 磨损:{a}")
                    tmp = item(buff_item.name,float(a),float(b),c)
                    result.append(tmp)
                    print(f"花费时间:{time()-start}s")
    return result

def create_item_lists_from_buff_item_list(buff_item_list:list[buff_item]):
    value = []
    count = 0 
    for i in buff_item_list:
        tmp = generate_item_list_from_buff_item(i)
        if tmp !=1:
            for j in tmp:
                value.append(j)
        count = count + 1
        print(f"已经完成:{count} items , 总数量:{len(buff_item_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(buff_item_list))}")
        sleep(sleeptime)
    write_item_to_json(value)
    print("finish")
    return value

def create_item_lists_from_deep_partition_list(deep_partition_list:list[deep_partition]):
    value = []
    count = 0 
    for i in deep_partition_list:
        tmp = generate_item_list_from_deep_partition(i)
        if tmp !=1:
            for j in tmp:
                value.append(j)
        count = count + 1
        print(f"item_list 已经完成:{count}, 总数量:{len(deep_partition_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(deep_partition_list))}")
        sleep(sleeptime)

    write_item_to_json(value)
    print("finish")
    return value

