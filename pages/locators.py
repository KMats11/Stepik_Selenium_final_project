from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators():
    PRODUCTS_IN_BASKET = (By.XPATH, "//form[@id='basket_formset']")
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div[@id='content_inner']/p")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ADDED_PRODUCT_NAME = (By.XPATH, "//div[@class='alertinner ']/strong")
    BASKET_TOTAL_PRICE = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_NAME = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='col-sm-6 product_main']/p[@class='price_color']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")
