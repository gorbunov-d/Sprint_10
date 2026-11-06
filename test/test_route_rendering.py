import allure
import pytest

from data import ADDRESS_PAIRS


@allure.feature("Отрисовка маршрута")
class TestRouteRendering:
    @allure.title("Две точки начала и конца на карте: {origin} → {destination}")
    @pytest.mark.parametrize("origin,destination", ADDRESS_PAIRS)
    def test_two_route_markers(self, route_page, origin, destination):
        route_page.fill_addresses(origin, destination)
        assert route_page.map_marker_count() == 2
