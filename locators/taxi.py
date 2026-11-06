from selenium.webdriver.common.by import By


class TaxiLocators:
    PANEL = (By.CSS_SELECTOR, ".tariff-picker.shown")
    TITLES = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard-title")
    ACTIVE_CARDS = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard.active")
    ACTIVE_TITLE = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard.active .tcard-title")
    ACTIVE_PRICE = (By.CSS_SELECTOR, ".tariff-picker.shown .tcard.active .tcard-price")
    PHONE = (By.CSS_SELECTOR, ".tariff-picker.shown .np-text")
    PAYMENT = (By.CSS_SELECTOR, ".tariff-picker.shown .pp-text")
    PAYMENT_VALUE = (By.CSS_SELECTOR, ".tariff-picker.shown .pp-value-text")
    COMMENT_LABEL = (By.CSS_SELECTOR, ".tariff-picker.shown label[for='comment']")
    REQUIREMENTS = (By.CSS_SELECTOR, ".tariff-picker.shown .reqs-head")
    REQUIREMENTS_HEADER = (By.CSS_SELECTOR, ".tariff-picker.shown .reqs-header")
    LAPTOP_SWITCH = (
        By.XPATH,
        "//div[contains(@class,'tariff-picker') and contains(@class,'shown')]//div[@class='r-sw-container'][div[normalize-space()='Столик для ноутбука']]//div[@class='switch']",
    )
    LAPTOP_INPUT = (
        By.XPATH,
        "//div[contains(@class,'tariff-picker') and contains(@class,'shown')]//div[@class='r-sw-container'][div[normalize-space()='Столик для ноутбука']]//input",
    )
    SUBMIT = (By.CSS_SELECTOR, ".smart-button")
    SUBMIT_LABEL = (By.CSS_SELECTOR, ".smart-button-main")
    FIELDS = [PHONE, PAYMENT, COMMENT_LABEL, REQUIREMENTS]

    @staticmethod
    def card(name):
        return (
            By.XPATH,
            f"//div[contains(@class,'tariff-picker') and contains(@class,'shown')]//div[contains(concat(' ',@class,' '),' tcard ')][div[@class='tcard-title' and text()='{name}']]",
        )

    @classmethod
    def info(cls, name):
        by, path = cls.card(name)
        return by, path + "//button[contains(@class,'i-button')]"

    @staticmethod
    def tooltip_description(index):
        return By.CSS_SELECTOR, f"#tariff-card-{index}.show .i-dPrefix"
