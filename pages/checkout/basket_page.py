from playwright.sync_api import Page

from pages.checkout.checkout_page import CheckoutPage


class BasketPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.checkout_button = page.locator('#checkout')

    def go_to_checkout(self) -> CheckoutPage:
        self.checkout_button.click()
        return CheckoutPage(self.page)
