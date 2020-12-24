
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.checkOutpage import checkOutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    username = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "[name='email']")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.CSS_SELECTOR, "select[class*='form-control']")
    rad = (By.CSS_SELECTOR,"label[class*='form-check-label']")
    rad_match= (By.CSS_SELECTOR, "input[class*='form-check-input']")
    submit = (By.CSS_SELECTOR, "input[type = 'submit']")
    success_text =(By.CSS_SELECTOR, "div.alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()
        checkout_Page = checkOutPage(self.driver)
        return checkout_Page
    #self.driver.find_element_by_css_selector("a[href*='shop']").click()

    def get_username(self):
        return self.driver.find_element(*HomePage.username)

    def get_emailadd(self):
        return self.driver.find_element(*HomePage.email)

    def g_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def g_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def sel_radio(self):
        return self.driver.find_elements(*HomePage.rad)

    def matched_radio(self):
        return self.driver.find_elements(*HomePage.rad_match)

    def submit_from(self):
        return self.driver.find_element(*HomePage.submit)

    def success_msg(self):
        return self.driver.find_element(*HomePage.success_text)



