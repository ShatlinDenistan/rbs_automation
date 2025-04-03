import os

import pytest
from playwright.sync_api import Page, Browser, Playwright
from pages.retail_portal.login_page import LoginPage
from tests.ui.retail.retail_test_base import RetailTestBase


@pytest.fixture(scope="function")
def test_init_without_logging_in(playwright: Playwright, request):
    """Test fixture to initialize the test without logging in."""
    browser: Browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page
    RetailTestBase().init_page_objects(request)
    retail_portal_home = os.getenv("RETAIL_PORTAL_HOME")
    page.goto(retail_portal_home)
    yield page
    context.close()
    browser.close()


@pytest.fixture(scope="function")
def test_init(playwright: Playwright, request):
    """Test fixture to initialize the test without logging in."""
    browser: Browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page: Page = context.new_page()
    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page
    RetailTestBase().init_page_objects(request)
    retail_portal_home = os.getenv("RETAIL_PORTAL_HOME")
    page.goto(retail_portal_home)
    LoginPage(page).login()

    yield page
    context.close()
    browser.close()
