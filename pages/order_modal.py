import re

import allure
from selenium.webdriver.support import expected_conditions as EC

from locators.order import OrderLocators as L
from pages.base_page import BasePage


class OrderModal(BasePage):
    @allure.step("Дождаться окна поиска машины")
    def wait_searching(self):
        self.visible(L.MODAL)
        self.wait(EC.text_to_be_present_in_element(L.TITLE, "Поиск машины"))
        self.wait(lambda _: self.timer_seconds() > 0)
        return self

    def title(self):
        return self.text(L.TITLE)

    def timer_seconds(self):
        minutes, seconds = self.text(L.TIMER).split(":")
        return int(minutes) * 60 + int(seconds)

    @allure.step("Проверить уменьшение таймера поиска")
    def wait_timer_decrease(self, initial):
        self.wait(lambda _: self.timer_seconds() < initial)
        return self.timer_seconds()

    def buttons_enabled(self):
        return [self.visible(L.button(label)).is_enabled() for label in ["Отменить", "Детали"]]

    @allure.step("Дождаться окончания поиска без ускорения таймера")
    def wait_assigned(self):
        self.wait(
            lambda _: re.fullmatch(r"\d+ мин\. и приедет", self.title()), "Поиск не завершился за 90 секунд", timeout=90
        )
        self.visible(L.NUMBER)
        return self

    def car_number(self):
        return self.text(L.NUMBER)

    def car_image_loaded(self):
        return self.image_loaded(L.CAR_IMAGE)

    def driver_name(self):
        return self.text(L.DRIVER_GROUP).splitlines()[-1]

    def driver_photo_loaded(self):
        return self.image_loaded(L.DRIVER_PHOTO)

    def driver_rating(self):
        return self.text(L.RATING)

    @allure.step("Открыть детали поездки")
    def open_details(self):
        self.click(L.button("Детали"))
        self.visible(L.DETAILS)

    def addresses_and_payment(self):
        return tuple(self.text(L.detail(label)) for label in ["Адрес подачи", "Адрес назначения", "Способ оплаты"])

    def trip_cost(self):
        return int(re.sub(r"\D", "", self.text(L.COST)))

    def trip_cost_text(self):
        return self.text(L.COST)

    @allure.step("Отменить заказ")
    def cancel(self):
        self.click(L.button("Отменить"))

    def is_closed(self):
        return self.wait(EC.invisibility_of_element_located(L.MODAL))
