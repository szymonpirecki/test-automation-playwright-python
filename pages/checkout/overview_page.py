from playwright.sync_api import Page

from pages.checkout.confirmation_page import ConfirmationPage


class OverviewPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.finish_button = page.locator('#finish')

    def confirm_purchase(self) -> ConfirmationPage:
        self.finish_button.click()
        return ConfirmationPage(self.page)
