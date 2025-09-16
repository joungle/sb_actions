import os
from seleniumbase import SB

USER = os.environ["USER"]
PW = os.environ["PW"]
MISSION = os.environ["MISSION"]

with SB(uc=True, incognito=True, xvfb=True, test=True, locale_code="de") as sb:
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
    sb.sleep(1)
    sb.driver.cdp.click("a#rescuetrack.singleLoginProvider")
    sb.sleep(2)
    sb.driver.cdp.open("https://apps.rescuetrack.com/rmp/")
    sb.sleep(3)
    sb.driver.cdp.click(f'div.button.assignButton[data-target="#assignTransportModal{MISSION}"]')
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    print(sb.cdp.get_element_rect(f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div', timeout=None))
    print(sb.cdp.get_element_size(f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div', timeout=None))
    print(sb.cdp.get_element_position(f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div', timeout=None))
    # sb.uc_gui_click_captcha()
    # sb.driver.cdp.gui_click_element(f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div')
    # sb.uc_gui_click_cf(frame=f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div', retry=False, blind=False)
    # sb.uc_gui_click_captcha()
    sb.cdp.gui_click_element(f'#assignTransportModal{MISSION} .modal-content #captchaWrapper div')
    sb.sleep(4)
    sb.save_screenshot_to_logs()
    print("Success! Website did not detect SeleniumBase!")
