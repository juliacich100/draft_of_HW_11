import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def desktop_browser_management():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    yield
    browser.quit()


@pytest.fixture(scope='function')
def mobile_browser_management():
    browser.config.window_height = 914
    browser.config.window_width = 412
    yield
    browser.quit()