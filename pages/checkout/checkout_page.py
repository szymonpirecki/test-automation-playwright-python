from __future__ import annotations

from playwright.sync_api import Page

from models.checkout_data_model import CheckoutDataModel
from pages.checkout.overview_page import OverviewPage


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.first_name_input = page.locator('#first-name')
        self.last_name_input = page.locator('#last-name')
        self.post_code_input = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')

    def fill_checkout_data(self, checkout_data: CheckoutDataModel) -> CheckoutPage:
        self.first_name_input.fill(checkout_data.first_name)
        self.last_name_input.fill(checkout_data.last_name)
        self.post_code_input.fill(checkout_data.post_code)
        return self

    def go_to_overview(self) -> OverviewPage:
        self.continue_button.click()
        return OverviewPage(self.page)
