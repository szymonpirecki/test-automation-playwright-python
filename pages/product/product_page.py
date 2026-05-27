from playwright.sync_api import Page

from pages.product.product_base_page import ProductBasePage


class ProductPage(ProductBasePage):
    def __init__(self, page: Page) -> None:
        self.page = page
        super().__init__(page.locator('[data-test="inventory-item"]'))
