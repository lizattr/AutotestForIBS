from locators import *


class Base:
    def __init__(self, driver):
        self.driver = driver

    def open_browser(self):
        self.driver.maximize_window()
        self.driver.get(base_url)

    def quit_browser(self):
        self.driver.quit()
