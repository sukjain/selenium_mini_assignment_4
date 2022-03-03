from datetime import time
from selenium import webdriver

from selenium.webdriver.chrome import webdriver

from Config.config import TestData

from selenium.webdriver.common.by import By

from Pages.Buy_Moisturizers import Moisturizers
from Pages.Buy_Sunscreeen import Sunscreen


class HomePage():

    def __init__(self, driver):
        self.driver=driver


    Temp = '//div[@id="weather"]'
    help_icon = "//span[@data-toggle='popover']"
    popover_body = "//div[@class='popover-body']"
    moisturizer_btn = "//button[text()='Buy moisturizers']"
    sunscreen_btn =  '//button[text()="Buy sunscreens"]'
    product_details = '//p[@class="font-weight-bold top-space-10"]'
    Add_btn = "//button[text()='Add']"

    def get_temp(self):
        temp = self.driver.find_element(By.XPATH, '//div[@id="weather"]').text
        return temp

    def convert_into_int(self,temp_value):
        numbers = []
        for word in temp_value.split():
            if word.isdigit():
                numbers.append(int(word))
        lst_str = str(numbers)[1:-1]
        temp1 = int(lst_str)
        return temp1


    def check_temp_and_perform_action(self,temp1):
        if (temp1 < 19):
            print("Mositurizer Page")
            text = "Moisturizers"
            self.driver.find_element(By.XPATH, '//button[text()="Buy moisturizers"]').click()
            return text

        else:
            print("Sunscreens Page")
            text = "Sunscreens"
            self.driver.find_element(By.XPATH, '//button[text()="Buy sunscreens"]').click()
            return text
