import time
from selenium.webdriver.common.by import By
class liga:
    def __init__(self, browser):
        self.browser = browser
    def prem(self):
        x = self.browser.find_element(By.XPATH,"//img[@alt='الدوري الألماني الدرجة الأولى']")
        x.click()
        time.sleep(4)