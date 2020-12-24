import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.checkOutpage import checkOutPage
from pageObjects.homePage import HomePage

#@pytest.mark.usefixtures("setup")
from utilities.baseclass import BaseClass



class Test001(BaseClass):
    def test_e2e(self):
        home_Page = HomePage(self.driver)
        checkout_Page = home_Page.shop_items()
        log = self.get_logger()
        # checkout_Page = checkOutPage(self.driver)
        log.info("getting card tittiles")
        cards = checkout_Page.get_titles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)

            if cardText == "Blackberry":
                checkout_Page.get_footer()[i].click()

        checkout_Page.items_checkout().click()

        confirm_page = checkout_Page.final_checkout()
        log.info("entering country as ind")
        confirm_page.country_name().send_keys('ind')

        self.wait_for_presence("India")
        confirm_page.pick_india().click()

        confirm_page.tick_checkbox().click()
        confirm_page.purchase().click()
        success_text = confirm_page.text_message().text
        log.info(success_text)
        assert "Success! Thank you! " in success_text

        self.driver.get_screenshot_as_file("screen.png")