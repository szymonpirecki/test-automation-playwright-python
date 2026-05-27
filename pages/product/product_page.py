from pages.product.product_base_page import ProductBasePage


class ProductPage(ProductBasePage):
    def __init__(self, page):
        self.page = page
        super().__init__(page.locator('[data-test="inventory-item"]'))
