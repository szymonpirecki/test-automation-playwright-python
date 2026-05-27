from playwright.sync_api import Page


class ConfirmationPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.confirmation_msg = page.locator('.complete-header')

    def get_confirmation_msg(self) -> str:
        return self.confirmation_msg.inner_text()
