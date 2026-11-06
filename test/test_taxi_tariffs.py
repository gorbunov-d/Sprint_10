import allure
import pytest

from data import CORRECT_TARIFF_CASES, KNOWN_BUG_TARIFF_CASES, ORDER_FIELDS, TARIFF_DESCRIPTIONS


@allure.feature("Заказ тарифа Такси")
class TestTaxiTariffs:
    @allure.title("Форма содержит шесть тарифов, ровно один выбран")
    def test_six_tariffs_and_one_active(self, taxi_page):
        assert taxi_page.tariff_names() == list(TARIFF_DESCRIPTIONS)
        assert len(taxi_page.active_tariffs()) == 1
        assert taxi_page.active_tariffs()[0] in TARIFF_DESCRIPTIONS

    @allure.title("Подсказка тарифа {name} соответствует ТЗ")
    @pytest.mark.parametrize("name,description", CORRECT_TARIFF_CASES)
    def test_tariff_tooltip(self, taxi_page, name, description):
        assert taxi_page.tariff_description(name) == description

    @allure.title("Подсказка тарифа {name} соответствует ТЗ — известный дефект")
    @pytest.mark.xfail(
        reason="BUG-001/BUG-002: описания Сонного и Разговорчивого переставлены местами", raises=AssertionError
    )
    @pytest.mark.parametrize("name,description", KNOWN_BUG_TARIFF_CASES)
    def test_known_incorrect_tariff_tooltip(self, taxi_page, name, description):
        assert taxi_page.tariff_description(name) == description

    @allure.title("Под тарифами отображаются все четыре поля заказа")
    def test_order_fields(self, taxi_page):
        assert taxi_page.order_fields() == ORDER_FIELDS
