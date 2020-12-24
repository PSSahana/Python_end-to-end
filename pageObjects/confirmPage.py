from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryId = (By.ID, "country")
    pick_country = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class= 'checkbox checkbox-primary']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def country_name(self):
        return self.driver.find_element(*ConfirmPage.countryId)

    def pick_india(self):
        return self.driver.find_element(*ConfirmPage.pick_country)

    def tick_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def text_message(self):
        return self.driver.find_element(*ConfirmPage.message)


