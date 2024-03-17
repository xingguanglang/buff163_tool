from playwright.sync_api import sync_playwright
from time import sleep
with sync_playwright() as p:
    # browser = p.chromium.launch_persistent_context("browser_buffer/chrome",headless=False)
    browser = p.chromium.connect_over_cdp("http://localhost:9222")
    page = browser.new_page()
    page.goto("https://buff.163.com/goods/33907#tab=selling&page_num=1&sort_by=paintwear.asc&min_paintwear=0.07&max_paintwear=0.08")
    page.wait_for_timeout(1<<30)
# with sync_playwright() as p:
#     password="Asd12345"
#     account = "13197425867"
#     # browser = p.chromium.launch_persistent_context("browser_buffer/chrome",headless=False)
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://buff.163.com/goods/33907#tab=selling&page_num=1&sort_by=paintwear.asc&min_paintwear=0.07&max_paintwear=0.08")
#     # a = page.get_by_text("Login with SMS" or "短信快捷登录").inner_html()
#     selector = "//iframe[contains(@id, 'x-URS-ifram')]"
#     selector1 = "//input[contains(@spellcheck,'false') and contains(@type,'tel')]"
#     selector2 = "//input[contains(@spellcheck,'false') and contains(@type,'password')]"
#     selector3 = "//input[contains(@type,'checkbox') and contains(@class,'dl-clause-login')]"
#     selector4 = "//a[contains(@tabindex,'8') and contains(@class,'u-loginbtn btncolor tabfocus ')]"
#     selector5 = "//a[contains(@href,'javascript:;') and contains(@onclick,'window.location.reload()')]"
#     # selector3 = "//span[contains(@class,'u-dl-agree-select') and contains(@id,'auto-id-')]"
#     try:
#         page.wait_for_selector(selector,timeout=3000)
#         iframe = page.frame_locator(selector)
#         passwordlogin = iframe.get_by_text("Login with password" or "短信快捷登录")
#         # b = iframe.locator(selector2).inner_text()
#         passwordlogin.click()
#         entertel = iframe.locator(selector1)
#         entertel.fill(account)
#         enterpassword = iframe.locator(selector2)
#         enterpassword.fill(password)
#         agree = iframe.locator(selector3)
#         agree.click()
#         login = iframe.locator(selector4)
#         login.click()
#         page.wait_for_selector(selector5,timeout=5000)
#         page.locator(selector5).all()[1].click()
#         # page.reload()
#     except:
#         print("err")
#     else:
#         print("success")
#         # print(
#     print("123123")
#     page.wait_for_timeout(1<<30)