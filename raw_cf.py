from seleniumbase import SB

with SB(uc=True, test=True, locale="en", guest=True) as sb:
    url = "https://www.cloudflare.com/login"
    sb.activate_cdp_mode(url)
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    sb.uc_gui_click_captcha()
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    cf_cookie = None
    all_cookies = sb.cdp.get_all_cookies()
    for cookie in all_cookies:
        if cookie.name == 'cf_clearance':
            cf_cookie = cookie
            break
    if cf_cookie:
        print("cf_clearance cookie: %s" % cf_cookie.value)
    else:
        print("Didn't find the cf_clearance cookie!")
