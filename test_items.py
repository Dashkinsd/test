link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_language_es(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("form[id='add_to_basket_form']>button[type='submit']")
    assert button is not None

