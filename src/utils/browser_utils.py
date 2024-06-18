from playwright.sync_api import sync_playwright


def init_browser(browser_name, headless=False):
    pr = sync_playwright().start()
    match browser_name:
        case "chrome":
            browser = pr.chromium.launch(channel="chrome", headless=headless)

        case "firefox":
            browser = pr.firefox.launch(headless=headless)
        case _:
            browser = pr.webkit.launch(headless=headless)

    return browser
