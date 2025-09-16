from seleniumbase import SB

with SB(uc=True, test=True, locale="en", guest=True) as sb:
    url = "https://www.cloudflare.com/login"
    sb.activate_cdp_mode(url)
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    sb.cdp.gui_click_element(".c_hh div div")
    # sb.uc_gui_click_captcha()
    sb.sleep(4)
    sb.save_screenshot_to_logs()
