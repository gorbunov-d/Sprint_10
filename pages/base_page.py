import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=15):
        self._driver = driver
        self._timeout = timeout

    def wait(self, condition, message="", timeout=None):
        return WebDriverWait(self._driver, timeout or self._timeout).until(condition, message)

    def visible(self, locator, timeout=None):
        return self.wait(EC.visibility_of_element_located(locator), f"Не виден элемент {locator}", timeout)

    def click(self, locator):
        self.wait(EC.element_to_be_clickable(locator)).click()

    def text(self, locator):
        return self.visible(locator).text.strip()

    def hover(self, locator):
        ActionChains(self._driver).move_to_element(self.visible(locator)).perform()

    def image_loaded(self, locator):
        image = self.visible(locator)
        return self._driver.execute_script("return arguments[0].complete && arguments[0].naturalWidth > 0", image)

    def attach_evidence(self):
        allure.attach(self._driver.get_screenshot_as_png(), "Экран при проверке", allure.attachment_type.PNG)
        allure.attach(self._driver.page_source, "DOM страницы", allure.attachment_type.HTML)
