import allure
import pytest

from data import MODE_SWITCHES, TRANSPORTS


@allure.feature("Подготовка к заказу такси")
class TestTaxiPreparation:
    @allure.title("Переключение {initial} → {target} меняет активный таб, цену и время")
    @pytest.mark.parametrize("initial,target", MODE_SWITCHES)
    def test_switching_route_recalculates(self, route_ready, initial, target):
        route_ready.choose_mode(initial)
        old_price, old_time = route_ready.route_summary()
        route_ready.choose_mode(target)
        route_ready.wait_summary_change((old_price, old_time))
        new_price, new_time = route_ready.route_summary()
        assert route_ready.active_mode() == target
        assert new_price != old_price
        assert new_time != old_time

    @allure.title("Свой: все шесть типов передвижения доступны")
    def test_custom_route_enables_all_transports(self, route_ready):
        route_ready.choose_mode("Свой")
        assert route_ready.active_mode() == "Свой"
        assert route_ready.transport_availability() == [True] * 6

    @allure.title("Свой: тип {transport} можно выбрать")
    @pytest.mark.parametrize("transport", TRANSPORTS)
    def test_custom_transport_can_be_selected(self, route_ready, transport):
        route_ready.choose_mode("Свой")
        route_ready.choose_transport(transport)
        assert route_ready.transport_active(transport)

    @allure.title("Быстрый: кнопка Вызвать такси активна")
    def test_fast_route_call_taxi_enabled(self, route_ready):
        route_ready.choose_mode("Быстрый")
        assert route_ready.taxi_button_enabled()

    @allure.title("Свой + Драйв: кнопка Забронировать активна")
    def test_custom_drive_booking_enabled(self, route_ready):
        route_ready.choose_mode("Свой")
        route_ready.choose_transport("Драйв")
        assert route_ready.booking_button_enabled()
