from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
    
    def get_element_text(self, elemento):
        return elemento.get_attribute("value")
    
    def get_alert_text(self):
        alert = Alert(self.driver)
        return alert.text
    
    def accept_alert(self):
        alert = Alert(self.driver)
        alert.accept()

    def wait_for_element(self, timeout, *locator):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))