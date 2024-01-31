import pytest
from playwright.sync_api import Page, expect

def test_main_navigation(page: Page):
    # Assertions use the expect API.
    expect(page).to_have_title('Orion')
def test_validate_username(page: Page):
    page.locator("input[type=\"text\"]").fill('Testing')
    page.locator("input[type=\"password\"]").fill('test')
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Unknown account"),'Error username').to_be_visible()

def test_validate_requerid(page: Page):
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Username *Required")).to_be_visible()
    expect(page.get_by_text("Password *Required")).to_be_visible()