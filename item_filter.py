from playwright.sync_api import sync_playwright,TimeoutError
from utils_storage import  write_item_to_json
from item import item,buff_item,deep_partition
from find_url import generate_goods_url,generate_goods_url_list
from datetime import datetime
from time import time,sleep
import threading
sleeptime = 5

def generate_item_list_from_buff_item(buff_item:buff_item, selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    url = generate_goods_url(buff_item)
    print("url:",url)
    with sync_playwright() as p:
        start = time()
        sleep(sleeptime)
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
    browser.close()
    return result

def generate_item_list_from_deep_partition(deep_partition,selector:str = '#market-selling-list > tbody>.selling',usr_data_dir = "browser_buffer/chrome"):
    urls = generate_goods_url_list(deep_partition)
    result = []
    password = 1
    account = 1
    selector6 = "//iframe[contains(@id, 'x-URS-ifram')]"
    selector1 = "//input[contains(@spellcheck,'false') and contains(@type,'tel')]"
    selector2 = "//input[contains(@spellcheck,'false') and contains(@type,'password')]"
    selector3 = "//input[contains(@type,'checkbox') and contains(@class,'dl-clause-login')]"
    selector4 = "//a[contains(@tabindex,'8') and contains(@class,'u-loginbtn btncolor tabfocus ')]"
    selector5 = "//a[contains(@href,'javascript:;') and contains(@onclick,'window.location.reload()')]"
    selector7 = "#remember-me > span > i"
    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(usr_data_dir,headless=True)
        page = browser.new_page()
        page.set_default_timeout(3000)
        for url in urls:
            sleep(sleeptime)
            start = time()
            try:
                page.goto(url)
                page.wait_for_selector(selector)
                print(time()-start,"s, 1")
            except(TimeoutError):
                try:
                    sleep(sleeptime)
                    page.reload()
                    page.wait_for_selector(selector)
                    print(time()-start,"s, 2")
                except:
                    print("error3")
                    return 2 
                    # try:
                    #     page.wait_for_selector(selector6)
                    #     print(time()-start,"s, 3")
                    #     iframe = page.frame_locator(selector6)
                    #     passwordlogin = iframe.get_by_text("Login with password" or "短信快捷登录")
                    #     passwordlogin.click()
                    #     print(time()-start,"s,4")
                    #     entertel = iframe.locator(selector1)
                    #     entertel.fill(account)
                    #     enterpassword = iframe.locator(selector2)
                    #     enterpassword.fill(password)
                    #     agree = iframe.locator(selector3)
                    #     agree.click()
                    #     page.wait_for_selector(selector7)
                    #     page.locator(selector7).click()
                    #     login = iframe.locator(selector4)
                    #     login.click()
                    #     print(time()-start,"s, 5")
                    #     page.wait_for_selector(selector5)
                    #     page.locator(selector5).all()[1].click()
                    #     print(123123)
                    #     print(time()-start,"s, 6")
                    #     page.wait_for_timeout(1<<30)
                        
                    # except:
                    #     print(time()-start,"s, 7")
                    #     return 2
                    # else:
                    #     print("登陆成功")
            except:
                print("other error")
                return 2
        

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
                    tmp = item(deep_partition.name,float(a),float(b),c)
                    result.append(tmp)
                    print(f"花费时间:{time()-start}s")
                    write_item_to_json(result)
    return result


def create_item_lists_from_buff_item_list(buff_item_list:list[buff_item]):
    value = []
    count = 0 
    for i in buff_item_list:
        tmp = generate_item_list_from_buff_item(i)
        if tmp !=2:
            for j in tmp:
                value.append(j)
        else:
            sleep(5)
        count = count + 1
        print(f"已经完成:{count} items , 总数量:{len(buff_item_list)}, 完成百分比:{'{:.2f}%'.format(count*100/len(buff_item_list))}")
        
    write_item_to_json(value)
    print("finish")
    return value


#parallel 
def create_item_lists_from_deep_partition_list(deep_partition_list:list[deep_partition],l_lens,total_cnt):
    value = []
    lock = threading.Lock()
    threads = []
    def process_partition(dp_list:list[deep_partition],cnt):
        tmp = generate_item_list_from_deep_partition(dp_list)
        with lock:
            try:
                if tmp!= 2:
                    for j in tmp:
                        value.append(j)
                    print(f"item_list 线程: {cnt}, 已经完成:{total_cnt}, 总数量:{l_lens}, 完成百分比:{'{:.2f}%'.format(total_cnt*100/l_lens)}")
        # 
            except:
                print("error2")
    cnt = 0
    for i in deep_partition_list:
    
        t = threading.Thread(target=process_partition,args=(i,cnt))
        t.start()
        threads.append(t)
        cnt += 1
    
    for t in threads:
        t.join()

    # write_item_to_json(value)
    return value


def create_item_main(dp_list:list[deep_partition]):
    count = 0
    tmp = [dp_list[0]]
    result = []
    cnt = 0
    for i in dp_list[1:] :
        cnt +=1
        if count<2: #n+1线程
            tmp.append(i)
            count += 1
        else:
            result.append(create_item_lists_from_deep_partition_list(tmp,len(dp_list),cnt))
            sleep(20)
            tmp = []
            tmp.append(i)
            count=0
    cnt+=1
    result.append(create_item_lists_from_deep_partition_list(tmp,len(dp_list),cnt))
    return result


if __name__ == "__main__":
    from utils_storage import read_deep_partition_from_json,read_deep_partition_from_all_json
    a = read_deep_partition_from_all_json()
    create_item_main(a)