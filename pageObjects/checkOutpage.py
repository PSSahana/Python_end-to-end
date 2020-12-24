from selenium.webdriver.common.by import By

from pageObjects.confirmPage import ConfirmPage


class checkOutPage:
    def __init__(self, driver):
        self.driver = driver


    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter =(By.CSS_SELECTOR, ".card-footer button")
    checkout1 = (By.CSS_SELECTOR, ".btn-primary")
    checkout2 =(By.XPATH, "//button[@class= 'btn btn-success']")

    def get_titles(self):
        return self.driver.find_elements(*checkOutPage.cardTitle)

    def get_footer(self):
        return self.driver.find_elements(*checkOutPage.cardFooter)

    def items_checkout(self):
        return self.driver.find_element(*checkOutPage.checkout1)

    def final_checkout(self):
        self.driver.find_element(*checkOutPage.checkout2).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page

