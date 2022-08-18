from selene.support.shared import browser
from selene import be, have

def search(value: str):
    browser.element('[name="q"]').should(be.blank).type(value).press_enter()


def test_search_link_selene(init_browser):
    search("selene")
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_no_have_link_selene(init_browser):
    search("selenoid")
    browser.element('[id="search"]').should(have.no.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
