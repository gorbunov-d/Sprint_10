import allure
import pytest

from data import ADDRESS_PAIRS, ADDRESSES, FREE_ROUTE


@allure.feature("Блок выбора маршрута")
class TestRouteSelection:
    @allure.title("Разные адреса показывают блок выбора маршрута")
    @pytest.mark.parametrize("origin,destination", ADDRESS_PAIRS)
    def test_route_panel_for_different_addresses(self, route_page, origin, destination):
        route_page.fill_addresses(origin, destination)
        assert route_page.panel_visible()

    @allure.title("Одинаковые адреса: Авто Бесплатно, В пути 0 мин.")
    @pytest.mark.parametrize("address", ADDRESSES)
    def test_same_address_free_route(self, route_page, address):
        route_page.fill_addresses(address, address)
        assert route_page.panel_visible()
        assert route_page.route_summary() == FREE_ROUTE
