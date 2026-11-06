import re

import allure

from data import ADDRESS_FROM, ADDRESS_TO, SEARCH_TITLE


@allure.feature("Сценарий заказа такси")
class TestTaxiOrderFlow:
    @allure.title("Рабочий + столик: кнопка Ввести номер и заказать открывает поиск")
    def test_search_window_and_countdown(self, laptop_taxi, order_modal):
        assert laptop_taxi.laptop_table_enabled()
        assert laptop_taxi.submit_label() == "Ввести номер и заказать"
        laptop_taxi.submit_order()
        order = order_modal.wait_searching()
        assert order.title() == SEARCH_TITLE
        assert order.buttons_enabled() == [True, True]
        initial = order.timer_seconds()
        assert order.wait_timer_decrease(initial) < initial

    @allure.title("Полный цикл: поиск, найденная машина, детали и отмена")
    def test_complete_taxi_order(self, laptop_taxi, searching_order):
        expected_price = laptop_taxi.selected_price()
        expected_payment = laptop_taxi.payment()
        assert searching_order.title() == SEARCH_TITLE
        assert searching_order.buttons_enabled() == [True, True]
        searching_order.wait_assigned()
        assert re.fullmatch(r"\d+ мин\. и приедет", searching_order.title())
        assert searching_order.car_number()
        assert searching_order.car_image_loaded()
        assert searching_order.driver_name()
        assert searching_order.driver_photo_loaded()
        assert re.fullmatch(r"[0-5][,.]\d", searching_order.driver_rating())
        assert searching_order.buttons_enabled() == [True, True]
        searching_order.open_details()
        assert searching_order.addresses_and_payment() == (ADDRESS_FROM, ADDRESS_TO, expected_payment)
        assert "Стоимость" in searching_order.trip_cost_text()
        assert searching_order.trip_cost() == expected_price
        searching_order.cancel()
        assert searching_order.is_closed()

    @allure.title("Отмена закрывает окно совершенного заказа")
    def test_cancel_assigned_order(self, assigned_order):
        assigned_order.cancel()
        assert assigned_order.is_closed()
