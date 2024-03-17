
def generate_buff_item_list_from_market_url(market_url:market_url):
    usr_data_dir = "browser_buffer/chrome"
    selector = "#j_list_card > ul > li"
    result = []
    password="Asd12345"
    selector = "#j_list_card > ul > li"
    account = "13197425867"
    selector = "//iframe[contains(@id, 'x-URS-ifram')]"
    selector1 = "//input[contains(@spellcheck,'false') and contains(@type,'tel')]"
    selector2 = "//input[contains(@spellcheck,'false') and contains(@type,'password')]"
    selector3 = "//input[contains(@type,'checkbox') and contains(@class,'dl-clause-login')]"
    selector4 = "//a[contains(@tabindex,'8') and contains(@class,'u-loginbtn btncolor tabfocus ')]"
    selector5 = "//a[contains(@href,'javascript:;') and contains(@onclick,'window.location.reload()')]"

    with sync_playwright() as p:
        start = time()
        sleep(sleeptime)
        browser = p.chromium.launch_persistent_context(usr_data_dir, headless=True)
        page = browser.new_page()
        try:
            page.goto(market_url.url)
            page.wait_for_selector(selector,timeout=5000)
        except(TimeoutError):
            try:
                sleep(sleeptime)
                page.reload()
                page.wait_for_selector(selector,timeout=5000)
            except:
                try:
                    page.wait_for_selector(selector,timeout=3000)
                    iframe = page.frame_locator(selector)
                    passwordlogin = iframe.get_by_text("Login with password" or "短信快捷登录")
                    passwordlogin.click()
                    entertel = iframe.locator(selector1)
                    entertel.fill(account)
                    enterpassword = iframe.locator(selector2)
                    enterpassword.fill(password)
                    agree = iframe.locator(selector3)
                    agree.click()
                    login = iframe.locator(selector4)
                    login.click()
                    page.wait_for_selector(selector5,timeout=5000)
                    page.locator(selector5).all()[1].click()
                except:
                    print(f"无法找到元素: 收藏品:{market_url.itemset[1]}, 等级:{market_url.quality[1]}, 外观:{market_url.exterior[1]}, 磨损:{market_url.rarity[1]}")

        print(f"url: {market_url.url}")
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
        write_buff_item_to_json(result)

    return result