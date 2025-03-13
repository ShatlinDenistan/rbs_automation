from playwright.sync_api import Page


class LoginPage:
    """login page objects"""

    def __init__(self, page: Page):
        self.user_name_textbox = page.get_by_role("textbox", name="Email")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login").nth(1)
