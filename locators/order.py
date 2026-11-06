from selenium.webdriver.common.by import By


class OrderLocators:
    MODAL = (By.CSS_SELECTOR, ".order.shown .order-body")
    TITLE = (By.CSS_SELECTOR, ".order.shown .order-header-title")
    TIMER = (By.CSS_SELECTOR, ".order.shown .order-header-time")
    NUMBER = (By.CSS_SELECTOR, ".order.shown .order-number .number")
    CAR_IMAGE = (By.CSS_SELECTOR, ".order.shown .order-number img")
    DRIVER_GROUP = (By.CSS_SELECTOR, ".order.shown .order-btn-group:first-child")
    DRIVER_PHOTO = (By.CSS_SELECTOR, ".order.shown .order-btn-group:first-child .order-button img")
    RATING = (By.CSS_SELECTOR, ".order.shown .order-btn-rating")
    DETAILS = (By.CSS_SELECTOR, ".order.shown .order-details.shown")
    COST = (
        By.XPATH,
        "//div[contains(@class,'order') and contains(@class,'shown')]//div[@class='order-details-content'][div[text()='Еще про поездку']]/div[@class='o-d-sh']",
    )

    @staticmethod
    def button(label):
        return (
            By.XPATH,
            f"//div[contains(@class,'order') and contains(@class,'shown')]//div[@class='order-btn-group'][div[normalize-space()='{label}']]/button",
        )

    @staticmethod
    def detail(label):
        return (
            By.XPATH,
            f"//div[contains(@class,'order-details') and contains(@class,'shown')]//div[@class='order-details-content'][div[@class='o-d-sh' and text()='{label}']]/div[@class='o-d-h']",
        )
