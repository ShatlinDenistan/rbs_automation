"""Test login functionality for the retail application."""

import os

import pytest
from tests.ui.retail.retail_test_base import RetailTestBase


@pytest.mark.usefixtures("test_init_without_logging_in")
class TestLogin(RetailTestBase):
    """Test login functionality for the retail application."""

    @pytest.mark.login
    def test_login_positive_scenario(self):
        """Test login functionality."""
        self.login_page.login()

    def test_login_without_password(self):
        """Test login without password."""
        self.login_page.login(password="", expected_to_login=False)

    def test_login_without_username(self):
        """Test login without username."""
        self.login_page.login(username="", expected_to_login=False)

    def test_login_with_invalid_username(self):
        """Test login with invalid username."""
        self.login_page.login(username="invalid_user", expected_to_login=False)

    def test_login_with_invalid_password(self):
        """Test login with invalid password."""
        self.login_page.login(password="invalid_password", expected_to_login=False)

    def test_login_with_invalid_username_and_password(self):
        """Test login with invalid username and password."""
        self.login_page.login(username="invalid_user", password="invalid_password", expected_to_login=False)

    def test_login_with_empty_username_and_password(self):
        """Test login with empty username and password."""
        self.login_page.login(username="", password="", expected_to_login=False)
