from playwright.sync_api import sync_playwright
from time import sleep
# with sync_playwright() as p:
    # browser = p.chromium.launch_persistent_context("browser_buffer/chrome",headless=False)
    # browser = p.chromium.connect_over_cdp("http://localhost:9222")
    # page = browser.new_page()
    # page.goto("https://buff.163.com/goods/33907#tab=selling&page_num=1&sort_by=paintwear.asc&min_paintwear=0.07&max_paintwear=0.08")
    # page.wait_for_timeout(1<<30)


with sync_playwright() as p:
    password="" #自己填
    account = ""
    # browser = p.chromium.launch_persistent_context("browser_buffer/chrome",headless=False)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://buff.163.com/market/csgo#game=csgo&page_num=1&rarity=common_weapon&quality=normal&exterior=wearcategory4&itemset=set_assault&tab=selling")
    # a = page.get_by_text("Login with SMS" or "短信快捷登录").inner_html()
    print(123123)
    page.wait_for_timeout(1<<30)
    selector6 = "//iframe[contains(@id, 'x-URS-ifram')]"
    selector1 = "//input[contains(@spellcheck,'false') and contains(@type,'tel')]"
    selector2 = "//input[contains(@spellcheck,'false') and contains(@type,'password')]"
    selector3 = "//input[contains(@type,'checkbox') and contains(@class,'dl-clause-login')]"
    selector4 = "//a[contains(@tabindex,'8') and contains(@class,'u-loginbtn btncolor tabfocus ')]"
    selector5 = "//a[contains(@href,'javascript:;') and contains(@onclick,'window.location.reload()')]"
    selector7 = "#remember-me > span > i"
        # print(time()-start,"s, 1")
    page.wait_for_selector(selector6)
    # print(time()-start,"s, 3")
    iframe = page.frame_locator(selector6)
    passwordlogin = iframe.get_by_text("Login with password" or "短信快捷登录")
    passwordlogin.click()
    # print(time()-start,"s,4")
    entertel = iframe.locator(selector1)
    entertel.fill(account)
    enterpassword = iframe.locator(selector2)
    enterpassword.fill(password)
    agree = iframe.locator(selector3)
    agree.click()
    page.wait_for_selector(selector7,timeout=2000)
    page.locator(selector7).click()
    login = iframe.locator(selector4)
    login.click()
    # print(time()-start,"s, 5")
    page.wait_for_selector(selector5)
    page.locator(selector5).all()[1].click()
    # print(time()-start,"s, 6")

    print("123123")
    page.wait_for_timeout(1<<30)
    