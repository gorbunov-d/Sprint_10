import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import ADDRESS_FROM, ADDRESS_TO, BASE_URL
from pages.base_page import BasePage
from pages.order_modal import OrderModal
from pages.route_page import RoutePage
from pages.taxi_page import TaxiPage


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="Показывать окно Chrome")
    parser.addoption("--base-url", default=BASE_URL)


@pytest.fixture
def browser(request):
    os.environ.setdefault("SE_SKIP_DRIVER_IN_PATH", "true")
    options = Options()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1100")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()


@pytest.fixture
def route_page(browser, request):
    return RoutePage(browser).open(request.config.getoption("--base-url"))


@pytest.fixture
def route_ready(route_page):
    route_page.fill_addresses(ADDRESS_FROM, ADDRESS_TO)
    return route_page


@pytest.fixture
def taxi_page(browser, route_ready):
    route_ready.choose_mode("Быстрый")
    route_ready.call_taxi()
    return TaxiPage(browser).wait_loaded()


@pytest.fixture
def laptop_taxi(taxi_page):
    taxi_page.choose_tariff("Рабочий")
    taxi_page.enable_laptop_table()
    return taxi_page


@pytest.fixture
def order_modal(browser):
    return OrderModal(browser)


@pytest.fixture
def searching_order(order_modal, laptop_taxi):
    laptop_taxi.submit_order()
    return order_modal.wait_searching()


@pytest.fixture
def assigned_order(searching_order):
    return searching_order.wait_assigned()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.failed and "browser" in item.funcargs:
        BasePage(item.funcargs["browser"]).attach_evidence()


def pytest_sessionfinish(session, exitstatus):
    results = session.config.getoption("allure_report_dir")
    if results:
        path = Path(results)
        path.mkdir(parents=True, exist_ok=True)
        (path / "environment.properties").write_text(
            f"Browser=Google Chrome\nBase.URL={session.config.getoption('base_url')}\nFramework=pytest + Selenium\n",
            encoding="utf-8",
        )
