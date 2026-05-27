from playwright.sync_api import Locator
from models.product_model import ProductModel


class ProductBasePage:
    def __init__(self, container: Locator):
        self.container = container
        self.product_title = container.locator('[data-test="inventory-item-name"]')
        self.product_price = container.locator('[data-test="inventory-item-price"]')
        self.product_description = container.locator('[data-test="inventory-item-desc"]')
        self.add_to_basket_button = container.locator('.btn_inventory')

    def get_product_title(self):
        return self.product_title.inner_text()

    def get_product_price(self):
        price_text = self.product_price.inner_text()
        return parse_price(price_text)

    def get_product_description(self):
        return self.product_description.inner_text()

    def map_to_product_model(self):
        return ProductModel(
            self.get_product_title(),
            self.get_product_price(),
            self.get_product_description()
        )


def parse_price(price_string):
    return float(price_string.replace('$', '').strip())
