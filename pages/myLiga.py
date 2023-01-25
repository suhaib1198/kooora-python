from selenium.webdriver.common.by import By
import time
class myliga:
    def __init__(self, browser):
        self.browser = browser
    def score(self):
        x = self.browser.find_element(By.LINK_TEXT, "الهدافين")
        time.sleep(5)
        x.click()
        time.sleep(5)
