import os
from seleniumbase import SB

USER = os.environ["USER"]
PW = os.environ["PW"]

with SB(uc=True, test=True, locale_code="de") as sb:
    sb.activate_cdp_mode("https://login.rescuetrack.com/login/login.html")
    sb.sleep(1)
    sb.driver.cdp.click("input#login-username")
    sb.driver.cdp.press_keys("input#login-username", USER)
    sb.driver.cdp.click("input#login-password")
    sb.driver.cdp.press_keys("input#login-password", PW)
    sb.sleep(2)
    sb.driver.cdp.click("login-button")
    sb.sleep(2)
    sb.driver.cdp.open("https://apps.rescuetrack.com/rmp/")
    sb.sleep(3)
    sb.driver.cdp.click(f'div.button.assignButton[data-target="#assignTransportModal71154072"]')
    sb.sleep(1)
    sb.uc_gui_click_captcha()
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    print("Success! Website did not detect SeleniumBase!")
