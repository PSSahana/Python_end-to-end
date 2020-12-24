import time

import pytest

from TestData.homePageData import HomePageData
from pageObjects.homePage import HomePage
from utilities.baseclass import BaseClass


class Test_002(BaseClass):

    def test_LoginPage(self, get_data):
        homepage = HomePage(self.driver)
        log = self.get_logger()
        homepage.get_username().send_keys(get_data["name"])
        homepage.get_emailadd().send_keys(get_data["email"])
        homepage.g_checkbox().click()
        self.select_option_by_text(homepage.g_gender(), get_data["gender"])
        radios = homepage.sel_radio()

        i = -1
        for radio in radios:
            i = i + 1
            radios_text = radio.text
            if radios_text == "Employed":
                homepage.matched_radio()[i].click()

        homepage.submit_from().click()
        success_text = homepage.success_msg().text
        log.info("loginpage " + success_text)

        assert "Success!" in success_text

        self.driver.refresh()
        time.sleep(10)

    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param








