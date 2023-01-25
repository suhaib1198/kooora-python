import time
from selenium.webdriver.common.by import By
class Base:
    def __init__(self,browser):
        self.browser = browser
    def title(self):
       return self.browser.title
    def scroll(self):
        self.browser.find_element(By.LINK_TEXT, "الرئيسية").click()
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(10)
        self.browser.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        time.sleep(10)
