import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_add_to_basket_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    assert button is not None, "Button was not found!"
    time.sleep(30)
