from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button_add.click()

    def should_be_basket_added_messages(self):
        self.should_be_right_name_of_added_to_basket_product()
        self.should_be_right_total_basket_price()

    def should_be_right_name_of_added_to_basket_product(self):
        added_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert added_name == product_name, 'wrong name of added product'

    def should_be_right_total_basket_price(self):
        # реализуйте проверку, что Стоимость корзины совпадает с ценой товара.
        basket_total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert basket_total_price == product_price, 'wrong basket total price'
