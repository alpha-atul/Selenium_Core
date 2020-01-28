from selenium.webdriver.support.events import AbstractEventListener


class MyListeners(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to")
        print(url)

    def after_navigate_to(self, url, driver):
        print("After navigate to")
        print(url)