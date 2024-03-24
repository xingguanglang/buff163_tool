from playwright.sync_api import sync_playwright,TimeoutError
from utils_storage import  write_item_to_json
from item import item,buff_item,deep_partition
from find_url import generate_goods_url,generate_goods_url_list
from datetime import datetime
from time import time,sleep

sleeptime = 1
import threading
sleeptime = 3




def process_url(itemsets,url,deep_partition,result,lock,selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    start = time()
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
        page = browser.new_page()
        try :
            page.goto(url)
        except(TimeoutError):
            1
        try:
            page.wait_for_selector(selector,timeout=2000)
        except(TimeoutError):
            times = 4
            while (True):
                sleep(8)
                page.reload()
                try:
                    page.wait_for_selector(selector,timeout=2000)
                except(TimeoutError):
                    print("url:",url)
                    print(f"找不到元素: 名字:{deep_partition.name}, buff_id:{deep_partition.buff_id}, 等级:{deep_partition.rarity}, 外观:{deep_partition.exterior}, 收藏品:{deep_partition.itemset}, 花费时间:{time()-start}s")
                    if times == 0:
                        return 1
                    times = times - 1
                else:
                    break
        value = page.locator(selector).all()
        print("url:",url)
        print(f"找到元素: 名字:{deep_partition.name}, buff_id:{deep_partition.buff_id}, 等级:{deep_partition.rarity}, 外观:{deep_partition.exterior}, 收藏品:{deep_partition.itemset}")
        for y in range(len(value)):
            i = value[y]
            if y <3:
                a = i.locator("td:nth-child(3) > div > div.csgo_value > div.wear-value").inner_text().split(" ")[1]
                b = i.locator(" td:nth-child(5) > div:nth-child(1) > strong").inner_text().split(" ")[1]
                c = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
                print(f"价格:{b}, 磨损:{a}")
                tmp = item(deep_partition.name,float(a),float(b),itemsets,c)
                with lock:
                    result.append(tmp)
                print(f"花费时间:{time()-start}s")
    return

def generate_item_list_from_deep_partition(deep_partition:deep_partition, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    tmp = generate_goods_url_list(deep_partition=deep_partition)[0]
    urls = tmp[0]
    itemsets = tmp[1]
    result = []
    lock = threading.Lock()

    threads = [threading.Thread(target=process_url,args=(itemsets,url,deep_partition,result,lock)) for url in urls]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("finish")
    return result


#parallel 
def create_item_lists_from_deep_partition_list(deep_partition_list:list[deep_partition]):
    value = []
    count = 0
    lock = threading.Lock()
    threads = []
    def process_partition(dp_list:list[deep_partition]):
        nonlocal count 
        tmp = generate_item_list_from_deep_partition(dp_list)
        with lock:
            try:
                for j in tmp:
                    value.append(j)
                count += 1
                print(f"item_list 已经完成:{count}, 总数量:{len(deep_partition_list)}, 完成百分比:{'{:.2f}%'.format(count[0]*100/len(deep_partition_list))}")
            except:
                1 
    cnt = 0
    for i in deep_partition_list:
        print("分区数:",cnt)
        t = threading.Thread(target=process_partition,args=(i,))
        t.start()
        threads.append(t)
        cnt += 1

    for t in threads:
        t.join()

    write_item_to_json(value)
    return value


def process_url_buffitem(itemsets,url,buff_item,result,lock,selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    start = time()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try :
            page.goto(url)
        except(TimeoutError):
            1
        try:
            page.wait_for_selector(selector,timeout=3000)
        except(TimeoutError):
            times = 2
            while (True):
                sleep(1)
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()
                try:
                    page.goto(url)
                    page.wait_for_selector(selector,timeout=3000)
                except(TimeoutError):
                    print("url:",url)
                    print(f"找不到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}, 花费时间:{time()-start}s")
                    if times == 0:
                        browser.close()
                        return 1
                    times = times - 1
                else:
                    break
        value = page.locator(selector).all()
        print("url:",url)
        print(f"找到元素: 名字:{buff_item.name}, buff_id:{buff_item.buff_id}, 等级:{buff_item.rarity}, 外观:{buff_item.exterior}, 收藏品:{buff_item.itemset}")
        for y in range(len(value)):
            i = value[y]
            if y <3:
                a = i.locator("td:nth-child(3) > div > div.csgo_value > div.wear-value").inner_text().split(" ")[1]
                b = i.locator(" td:nth-child(5) > div:nth-child(1) > strong").inner_text().split(" ")[1]
                c = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
                print(f"价格:{b}, 磨损:{a}")
                tmp = item(buff_item.name,float(a),float(b),itemsets,c)
                with lock:
                    result.append(tmp)
                print(f"花费时间:{time()-start}s")
    return

def generate_item_list_from_buff_item(buff_item:buff_item, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    tmp = generate_goods_url(buff_item)
    urls = tmp[0]
    itemsets = tmp[1]
    result = []
    lock = threading.Lock()

    threads = [threading.Thread(target=process_url_buffitem,args=(itemsets,url,buff_item,result,lock)) for url in urls]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("finish")
    return result


#parallel 
def create_item_lists_from_buff_item_list(buff_item_list:list[buff_item]):
    value = []
    count = 0
    lock = threading.Lock()
    threads = []
    def process_partition(bf_list:list[buff_item]):
        nonlocal count 
        tmp = generate_item_list_from_buff_item(bf_list)
        with lock:
            try:
                for j in tmp:
                    value.append(j)
                count += 1
                print(f"item_list 已经完成:{count}, 总数量:{len(buff_item_list)}, 完成百分比:{'{:.2f}%'.format(count[0]*100/len(buff_item_list))}")
            except:
                1 
    cnt = 0
    for i in buff_item_list:
        print("分区数:",cnt)
        t = threading.Thread(target=process_partition,args=(i,))
        t.start()
        threads.append(t)
        cnt += 1

    for t in threads:
        t.join()
    write_item_to_json(value)
    return value


def price_from_buff_item_without_login(step):
    a = read_buff_item_from_all_json()
    cnt = 0
    step = step
    for i in range(len(a)):
        if cnt == step:
            start = time()
            create_item_lists_from_buff_item_list(a[i-step:i])
            print(f"已完成:{i}, 总数量:{len(a), 完成百分比:{i/len(a)}, 此次时间:{time()-start}s}")
            cnt = 0
        cnt += 1
    return

if __name__ == "__main__":
    from utils_storage import read_deep_partition_from_all_json,read_buff_item_from_json
    from utils_storage import read_deep_partition_from_json,read_buff_item_from_all_json
    # a = read_deep_partition_from_json("json/deep_partitions_AWP | 九头金蛇 _.json")
    # a = read_deep_partition_from_all_json()[0:4]
    a = read_buff_item_from_all_json()
    # a = read_buff_item_from_json("json/buff_items_法玛斯 | 奈芙蒂斯之河 _.json")
    # print(a)
    # exit()
    # for i in a:
    cnt = 0
    step = 6
    for i in range(len(a)):
        if cnt == step:
            create_item_lists_from_buff_item_list(a[i-step:i])
            print
            cnt = 0
        cnt += 1
        # sleep(20)
