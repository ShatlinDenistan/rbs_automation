from playwright.sync_api import Page
import os


class LoginPage:
    """login page objects"""

    def __init__(self, page: Page):
        self.user_name_textbox = page.get_by_role("textbox", name="Email")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login").nth(1)

    def login(self, username=None, password=None, expected_to_login=True):
        """login to the application"""
        if username is None:
            username = os.getenv("USER_NAME")
        if password is None:
            password = os.getenv("PASSWORD")
        self.user_name_textbox.fill(username)
        self.password_textbox.fill(password)
        self.login_button.click()
        if expected_to_login:
            pass
            """Add code to assert that we have logged in successfully"""
