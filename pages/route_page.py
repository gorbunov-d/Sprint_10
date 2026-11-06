import allure
from selenium.webdriver.common.keys import Keys

from locators.routes import RouteLocators as L
from pages.base_page import BasePage


class RoutePage(BasePage):
    @allure.step("Открыть сервис маршрутов")
    def open(self, url):
        self._driver.get(url)
        self.visible(L.FROM)
        return self

    @allure.step("Построить маршрут: {origin} → {destination}")
    def fill_addresses(self, origin, destination):
        self.visible(L.FROM).send_keys(origin)
        self.visible(L.TO).send_keys(destination, Keys.TAB)
        self.visible(L.PANEL)
        self.visible(L.PRICE)

    @allure.step("Выбрать вид маршрута «{name}»")
    def choose_mode(self, name):
        self.click(L.mode(name))
        self.wait(lambda _: self.active_mode() == name)

    def active_mode(self):
        return self.text(L.ACTIVE_MODE)

    def route_summary(self):
        return self.text(L.PRICE), self.text(L.DURATION)

    def wait_summary_change(self, previous):
        self.wait(lambda _: self.route_summary() != previous)

    def panel_visible(self):
        return self.visible(L.PANEL).is_displayed()

    @allure.step("Дождаться двух видимых точек на карте")
    def map_marker_count(self):
        self.visible(L.MAP_CANVAS, timeout=40)
        self.wait(
            lambda d: len([e for e in d.find_elements(*L.MAP_MARKERS) if e.is_displayed()]) >= 2,
            "На карте не появились точки начала и конца маршрута",
            timeout=40,
        )
        return len([e for e in self._driver.find_elements(*L.MAP_MARKERS) if e.is_displayed()])

    def transport_availability(self):
        return ["disabled" not in e.get_attribute("class").split() for e in self._driver.find_elements(*L.TYPES)]

    @allure.step("Выбрать тип передвижения «{name}»")
    def choose_transport(self, name):
        self.click(L.transport(name))

    def transport_active(self, name):
        return "active" in self.visible(L.transport(name)).get_attribute("class").split()

    def taxi_button_enabled(self):
        return self.visible(L.CALL_TAXI).is_enabled()

    def booking_button_enabled(self):
        return self.visible(L.BOOK_DRIVE).is_enabled()

    @allure.step("Открыть заказ такси")
    def call_taxi(self):
        self.click(L.CALL_TAXI)
