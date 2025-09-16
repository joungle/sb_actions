from seleniumbase import SB

with SB(uc=True, test=True, locale="en", guest=True) as sb:
    url = "https://www.cloudflare.com/login"
    sb.activate_cdp_mode(url)
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    sb.uc_gui_click_captcha()  # PyAutoGUI click. (Linux needs it)
    sb.sleep(4)
    sb.save_screenshot_to_logs()
