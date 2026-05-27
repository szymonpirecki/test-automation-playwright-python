from playwright.sync_api import Page, Locator

from pages.product.product_base_page import ProductBasePage
from pages.product.product_page import ProductPage


class ProductContainerComponent(ProductBasePage):
    def __init__(self, page: Page, container: Locator) -> None:
        super().__init__(container)
        self.page = page

    def add_to_basket(self) -> None:
        self.add_to_basket_button.click()

    def go_to_product_page(self) -> ProductPage:
        self.product_title.click()
        return ProductPage(self.page)
