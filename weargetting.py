from playwright.sync_api import sync_playwright
from time import sleep
import json
gun_list = ["AK-47","M4A1-S","M4A4","AWP","FAMAS","AUG","SSG 08","Galil AR","SG 553", "G3SG1","SCAR-20","Glock-18"
            ,"USP-S","Tec-9","CZ75-Auto","Desert Eagle","Dual Berettas", "Five-SeveN","R8 Revolver","P2000"
            ,"P250","MP5-SD","P90","MP7","MP9","PP-Bizon","UMP-45","MAC-10","Sawed-Off","XM1014","Nova",
            "MAG-7","M249","Negev"
            ]
with sync_playwright() as p:
    minselector = "body > div.container.search-sec > div > div > div.panel-body > div.row.rulerrow > div > div.slider.slider-horizontal.slider-disabled > div.tooltip.tooltip-min.bottom.in > div.tooltip-inner"
    maxselector = "body > div.container.search-sec > div > div > div.panel-body > div.row.rulerrow > div > div.slider.slider-horizontal.slider-disabled > div.tooltip.tooltip-max.in.top > div.tooltip-inner"
    kuangselector = "body > div.container.search-sec > div > div > div.panel-body > div:nth-child(1) > div:nth-child(1) > div > button"
    kuang2selector= "body > div.container.search-sec > div > div > div.panel-body > div:nth-child(1) > div:nth-child(2) > div > button"
    selector = "body > div.container.search-sec > div > div > div.panel-body > div:nth-child(1) > div:nth-child(1) > div > div > ul > li:nth-child(4)"
    selector = "body > div.container.search-sec > div > div > div.panel-body > div:nth-child(1) > div:nth-child(1) > div > div > ul"
    browser = p.chromium.launch(headless=False)
    selector2 = "body > div.container.search-sec > div > div > div.panel-body > div:nth-child(1) > div:nth-child(2) > div > div > ul >li"
    selector3 = "#select_skin > //span[contains(@class,'text')]"
    selector4 = "//div[contains(@text,'最小值')]"
    # browser = p.chromium.launch_per(headless=False)
    page = browser.new_page()
    page.set_default_timeout(3000)
    page.goto("https://www.csgola.com/skinvideo/")
    # page.wait_for_selector(kuangselector,timeout=3000)
    # page.locator(kuangselector).click()
    # page.wait_for_selector(selector,timeout=3000)
    # a = page.locator(selector).inner_text()
    text = []
    for i in gun_list:
        page.wait_for_selector(kuangselector,timeout=3000)
        page.locator(kuangselector).click()
        sleep(0.2)
        page.locator("a").filter(has_text=i).click()
        page.wait_for_timeout(1<<30)
        # page.wait_for_selector(selector2,timeout=5000)
        # sleep(1)
        temp = page.locator(selector2).all()[1:]
        for j in temp:
            # sleep(0.5)
            page.wait_for_selector(kuang2selector,timeout=3000)
            page.locator(kuang2selector).click()
            if j.text_content() == "-选个皮肤-":
                continue
            j.click()
            print('j:',j.text_content())
            # sleep(0.5)
            result = j.text_content().split("|")[0]
            minwear = page.get_by_text("最小值: ").text_content()
            minwear = minwear.split(" ")[1]
            maxwear = page.get_by_text("最大值: ").text_content()
            maxwear = maxwear.split(" ")[1]
            print(i,result,minwear,maxwear)
            text.append({"name":str(i+" | "+result)[:-1],"minwear":minwear,"maxwear":maxwear})
    with open("磨损.json","w") as f:
        for i in text:
            tmp = json.dumps(i,ensure_ascii=False)
            f.write(tmp+'\n')

    # print(a)
    # print(len(a),a[3].get_attribute("class"),"ooo")
    # a[3].click()
    print("23232")
    
    # for i in range(1,len(a)):

    #     # page.wait_for_selector(kuangselector,timeout=3000)
    #     # page.locator(kuangselector).click()
    #     print(a[i].inner_html())
    #     page.wait_for_selector(selector2,timeout=3000)
    #     tmp = page.locator(selector2).all()
    #     sleep(1)
    #     for j in tmp:
    #         text.append(j.inner_text().split("|")[0])
    #         print(j.inner_text().split("|")[0])
        
    # page.goto("https://www.csgola.com/skinvideo/")
    # a = page.locator(selector).inner_html()
    # print(a)
    # a = page.get_by_text("Login with SMS" or "短信快捷登录").inner_html()
    print(123123)
    page.wait_for_timeout(1<<30)