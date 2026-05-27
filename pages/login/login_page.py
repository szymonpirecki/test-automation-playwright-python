class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_input = page.locator('#user-name')
        self.password_input = page.locator('#password')
        self.error_msg = page.locator('.error-message-container')

    def log_in(self, login_data):
        self.login_input.fill(login_data.username)
        self.password_input.fill(login_data.password)
        self.password_input.press('Enter')
        return self

    def get_error_msg(self):
        return self.error_msg.inner_text()
