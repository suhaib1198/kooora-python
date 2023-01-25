from selenium import webdriver
from pages.barPage import NavBar
from pages.laLiga import liga
from pages.base import Base
from pages.myLiga import myliga

class Home:
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        browser.maximize_window()
        self.browser.get("https://www.kooora.com")

    def test_title(self,name,title):
        try:
            assert name == title
        except:
            print("not same")


browser = webdriver.Chrome()
base = Base(browser)
home_page = Home(browser)
home_page.load()
bar = NavBar(browser)
bar.homeClick()
bar.todayClick()
title = base.title()
liga(browser).prem()
li = myliga(browser)
li.score()
base.scroll()
print(title)
home_page.test_title("مباريات اليوم", title)




