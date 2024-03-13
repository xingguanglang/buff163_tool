from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context("browser_buffer/chrome",headless=False)
    page = browser.new_page()
    page.goto("https://buff.163.com/goods/33907#tab=selling&page_num=1&sort_by=paintwear.asc&min_paintwear=0.07&max_paintwear=0.08")
    page.wait_for_timeout(3000000)