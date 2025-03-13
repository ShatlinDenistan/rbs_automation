import pytest

from playwright.sync_api import Playwright


class TestLogin:
    @pytest.mark.login
    def test_login(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False)
        admin_context = browser.new_context()
        page = admin_context.new_page()
        user_context = browser.new_context()
        user_page = user_context.new_page()
        page.goto("https://retail.master.env/")
        user_page.goto("https://retail.master.env/")

        page.get_by_role("textbox", name="Email").fill("shatlin.denistan@takealot.com")
        page.get_by_role("textbox", name="Password").fill("wrongpassword")
        page.get_by_role("button", name="Login").nth(1).click()

        user_page.get_by_role("textbox", name="Email").fill("shatlin.denistan@takealot.com")
        user_page.get_by_role("textbox", name="Password").fill("wrongpassword")
        user_page.get_by_role("button", name="Login").nth(1).click()

        # ---------------------
        admin_context.close()
        user_context.close()
        browser.close()
