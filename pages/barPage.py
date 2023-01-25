import time
from selenium.webdriver.common.by import By
class NavBar:
    def __init__(self, browser):
        self.browser = browser
    def homeClick(self):
       x = self.browser.find_element(By.LINK_TEXT, "الرئيسية")
       time.sleep(5)
       x.click
       time.sleep(5)
    def todayClick(self):
       x = self.browser.find_element(By.LINK_TEXT,"اليوم")
       time.sleep(5)
       x.click()
       time.sleep(4)
