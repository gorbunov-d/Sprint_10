import re

import allure

from data import TARIFF_DESCRIPTIONS
from locators.taxi import TaxiLocators as L
from pages.base_page import BasePage


class TaxiPage(BasePage):
    def wait_loaded(self):
        self.visible(L.PANEL)
        self.visible(L.ACTIVE_PRICE)
        self.wait(lambda d: len(d.find_elements(*L.TITLES)) == 6)
        return self

    def tariff_names(self):
        return [e.text for e in self._driver.find_elements(*L.TITLES)]

    def active_tariffs(self):
        return [e.text.splitlines()[0] for e in self._driver.find_elements(*L.ACTIVE_CARDS)]

    @allure.step("Навести на i тарифа «{name}»")
    def tariff_description(self, name):
        self.choose_tariff(name)
        self.hover(L.info(name))
        return self.text(L.tooltip_description(list(TARIFF_DESCRIPTIONS).index(name)))

    def order_fields(self):
        return [self.text(locator).rstrip(".") for locator in L.FIELDS]

    @allure.step("Выбрать тариф «{name}»")
    def choose_tariff(self, name):
        self.click(L.card(name))
        self.wait(lambda _: self.text(L.ACTIVE_TITLE) == name)

    @allure.step("Включить столик для ноутбука")
    def enable_laptop_table(self):
        self.click(L.REQUIREMENTS_HEADER)
        self.click(L.LAPTOP_SWITCH)
        self.wait(lambda d: d.find_element(*L.LAPTOP_INPUT).is_selected())

    def laptop_table_enabled(self):
        return self._driver.find_element(*L.LAPTOP_INPUT).is_selected()

    def selected_price(self):
        return int(re.sub(r"\D", "", self.text(L.ACTIVE_PRICE)))

    def payment(self):
        return self.text(L.PAYMENT_VALUE)

    def submit_label(self):
        return self.text(L.SUBMIT_LABEL)

    @allure.step("Нажать кнопку заказа")
    def submit_order(self):
        self.click(L.SUBMIT)
