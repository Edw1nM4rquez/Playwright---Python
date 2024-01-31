import pytest
from playwright.sync_api import sync_playwright, Page
import os

#
@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as playwright:
        yield playwright

#This function configures the screen browser with Chrome.
@pytest.fixture(scope="session")
def page(playwright):
    #You can set headless to true to show the browser and false to hide it.
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    #Timeout in miliseconds
    page.set_default_timeout(30000)
    yield page
    browser.close()

@pytest.fixture(scope="module", autouse=True)
def before_each_after_each(page: Page):
    print("before the test runs")
    # Go to the starting url before each test.
    page.goto("https://regtest.ui.orionic.com")
    yield
    print("after the test runs")

#Report path configuration
def pytest_configure(config):
    config.option.htmlpath = "html-report/reporte.html"

#Settings for screenshots when testing errors exist
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        try:
            page = item.funcargs["page"]
            screenshot_path = os.path.join("screenshots", f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            print(f"Screenshots: {screenshot_path}")
        except Exception as e:
            print(f"Dont can save screenshots: {e}")