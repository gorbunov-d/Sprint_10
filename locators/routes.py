from selenium.webdriver.common.by import By


class RouteLocators:
    FROM = (By.ID, "from")
    TO = (By.ID, "to")
    PANEL = (By.CSS_SELECTOR, ".type-picker.shown")
    ACTIVE_MODE = (By.CSS_SELECTOR, ".type-picker.shown .mode.active")
    PRICE = (By.CSS_SELECTOR, ".type-picker.shown .results-text .text")
    DURATION = (By.CSS_SELECTOR, ".type-picker.shown .duration")
    MAP = (By.ID, "map")
    MAP_CANVAS = (By.CSS_SELECTOR, "#map [class$='-map']")
    MAP_MARKERS = (By.CSS_SELECTOR, "#map [class*='-placemark-overlay']")
    TYPES = (By.CSS_SELECTOR, ".type-picker.shown .type")
    ACTIVE_TYPE = (By.CSS_SELECTOR, ".type-picker.shown .type.active img")
    CALL_TAXI = (
        By.XPATH,
        "//div[contains(@class,'type-picker') and contains(@class,'shown')]//button[normalize-space()='Вызвать такси']",
    )
    BOOK_DRIVE = (
        By.XPATH,
        "//div[contains(@class,'type-picker') and contains(@class,'shown')]//button[normalize-space()='Забронировать']",
    )
    TRANSPORT_KEYS = {
        "Машина": "car",
        "Пешком": "walk",
        "Такси": "taxi",
        "Велосипед": "bike",
        "Самокат": "scooter",
        "Драйв": "drive",
    }

    @staticmethod
    def mode(name):
        return By.XPATH, f"//div[contains(@class,'modes-container')]/div[normalize-space()='{name}']"

    @classmethod
    def transport(cls, name):
        key = cls.TRANSPORT_KEYS[name]
        return By.XPATH, f"//div[contains(@class,'types-container')]/div[img[contains(@src,'/static/media/{key}')]]"
