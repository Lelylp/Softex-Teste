import os, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from behave.model_core import Status

# Hooks
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 10)

def after_scenario(context, scenario):
    print(scenario.name)
    if scenario.status == Status.failed:
        # Tirar uma screenshot se o cenário falhar
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}.png")
        context.driver.save_screenshot(screenshot_path)
    yield context.driver
    context.driver.quit()