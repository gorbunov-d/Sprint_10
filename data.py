"""Ожидания из ТЗ, независимо от текущего поведения приложения."""

BASE_URL = "https://qa-routes.education-services.ru/"
ADDRESS_FROM = "Хамовнический вал, 34"
ADDRESS_TO = "Зубовский бульвар, 37"
ADDRESS_PAIRS = [(ADDRESS_FROM, ADDRESS_TO), (ADDRESS_TO, ADDRESS_FROM)]
ADDRESSES = [ADDRESS_FROM, ADDRESS_TO]
TARIFF_DESCRIPTIONS = {
    "Рабочий": "Для деловых особ, которых отвлекают",
    "Сонный": "Для тех, кто не выспался",
    "Отпускной": "Если пришла пора отдохнуть",
    "Разговорчивый": "Если мысли не выходят из головы",
    "Утешительный": "Если хочется свернуться калачиком",
    "Глянцевый": "Если нужно блистать",
}
TRANSPORTS = ["Машина", "Пешком", "Такси", "Велосипед", "Самокат", "Драйв"]
ORDER_FIELDS = ["Телефон", "Способ оплаты", "Комментарий водителю", "Требования к заказу"]
SEARCH_TITLE = "Поиск машины"
FREE_ROUTE = ("Авто Бесплатно", "В пути 0 мин.")

MODE_SWITCHES = [("Оптимальный", "Быстрый"), ("Быстрый", "Оптимальный")]
CORRECT_TARIFF_CASES = [
    (name, TARIFF_DESCRIPTIONS[name]) for name in ["Рабочий", "Отпускной", "Утешительный", "Глянцевый"]
]
KNOWN_BUG_TARIFF_CASES = [
    ("Сонный", TARIFF_DESCRIPTIONS["Сонный"]),
    ("Разговорчивый", TARIFF_DESCRIPTIONS["Разговорчивый"]),
]
