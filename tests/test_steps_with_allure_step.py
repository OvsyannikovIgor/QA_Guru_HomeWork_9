import allure
from selene import browser, by, have


def test_check_issue():
    with allure.step("Открываем главную страницу"):
        browser.open('/')
    with allure.step("Ищем репозитория"):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").type("OvsyannikovIgor/QA_Guru_HomeWork_9")
        browser.element("#query-builder-test").submit()
    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("OvsyannikovIgor/QA_Guru_HomeWork_9")).click()
    with allure.step("Открываем вкладку Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие текста на странице"):
        browser.element('.blankslate').should(
            have.text(("To get started, you should create an issue.")))
