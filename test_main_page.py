from selenium.webdriver.common.by import By
# from time import sleep


# def test_add_to_basket_button(browser):
#     browser.get(
#         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
#     button = browser.find_element(
#         By.CSS_SELECTOR,
#         "button[class='btn btn-lg btn-primary btn-add-to-basket']")
#     sleep(10)
#     assert button, 'No button here'

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
