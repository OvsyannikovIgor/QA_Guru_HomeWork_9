import allure
from allure_commons.types import Severity
from selene import browser
from selene import by, have
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "OvsyannikovIgor")
@allure.feature("Issue в репозитории")
@allure.story("Проверка наличия текста Issue")
@allure.link("https://github.com", name="Testing")
def test_to_check_issue():
    browser.open('/')

    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type("OvsyannikovIgor/QA_Guru_HomeWork_9")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("OvsyannikovIgor/QA_Guru_HomeWork_9")).click()

    browser.element("#issues-tab").click()

    browser.element('.blankslate').should(
        have.text(("To get started, you should create an issue.")))


