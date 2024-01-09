import allure
import pytest
from allure_commons.types import Severity
from selene import browser
from selene import by, have
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_width = 1200
    browser.config.window_height = 720
    browser.config.base_url = 'https://github.com'
    driver_options = webdriver.ChromeOptions()
    browser.config.driver_options = driver_options

    yield

    browser.quit()


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


def test_to_check_issue_allure_steps():
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


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('/')


@allure.step("Ищем репозиторий")
def search_for_repository(repo):
    browser.element(".header-search-button").click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем вкладку Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие текста на странице")
def should_have_text(text):
    browser.element('.blankslate').should(
        have.text((text)))


def test_decorator_allure_step():
    open_main_page()
    search_for_repository("OvsyannikovIgor/QA_Guru_HomeWork_9")
    go_to_repository("OvsyannikovIgor/QA_Guru_HomeWork_9")
    open_issue_tab()
    should_have_text("To get started, you should create an issue.")
