import pytest
from selene.support.shared import browser


@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 720

@pytest.fixture
def init_browser():
    browser.open('https://google.com')