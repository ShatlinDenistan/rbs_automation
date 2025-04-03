from json import load
import pytest
import re
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
import os
from pages.retail_portal.login_page import LoginPage

load_dotenv(override=True)


class TestLogin:
    @pytest.mark.login
    @pytest.mark.RBS_2122
    def test_login(self, playwright: Playwright):
        browser = playwright.chromium.launch(headless=False, slow_mo=2000)
        context = browser.new_context()
        page = context.new_page()
        retail_portal_home = "https://promotions.master.env/"
        user_name = os.getenv("USER_NAME")
        password = os.getenv("PASSWORD")
        page.goto(retail_portal_home)
        login_page = LoginPage(page)

        login_page.user_name_textbox.fill(user_name)
        login_page.password_textbox.fill(password)
        login_page.login_button.click()

        # ---------------------
        context.close()
        browser.close()
