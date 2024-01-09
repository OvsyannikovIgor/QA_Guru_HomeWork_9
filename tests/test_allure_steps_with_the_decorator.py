import allure
from selene import browser, have, by


@allure.step("Проверяем наличие текста на странице")
def should_have_text(text):
    browser.element('.blankslate').should(
        have.text((text)))


@allure.step("Открываем вкладку Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Переходим по ссылке репозитория")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Ищем репозиторий")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('/')


def test_to_check_issue():
    open_main_page()
    search_for_repository("OvsyannikovIgor/QA_Guru_HomeWork_9")
    go_to_repository("OvsyannikovIgor/QA_Guru_HomeWork_9")
    open_issue_tab()
    should_have_text("To get started, you should create an issue.")
