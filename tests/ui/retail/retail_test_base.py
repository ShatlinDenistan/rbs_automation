from playwright.sync_api import Page
from pages.retail_portal.login_page import LoginPage


class RetailTestBase:
    page: Page

    def init_page_objects(self, request) -> None:
        """
        Initialize the page objects for the test case.
        This method should be overridden by subclasses to initialize specific page objects.
        """
        self.page = request.cls.page
        self.login_page = request.cls.login_page = LoginPage(self.page)
