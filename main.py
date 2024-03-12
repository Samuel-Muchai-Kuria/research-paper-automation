from seleniumbase import BaseCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from seleniumbase import Driver
import time
import requests
import traceback
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz, process
from pynput.keyboard import Key, Controller
import json
import threading
from datetime import datetime


class Surfing(BaseCase):
    def setUp(self):
        super().setUp()
        with open("input.json","r") as f:
            self.data = json.load(f)
        self.action = ActionChains(self.driver)

    def webpage_check(self):
        for _ in range(31):
            if self.execute_script("return document.readyState") == "complete":
                break
            else:
                time.sleep(1)
    def texter(self,name, value,locator="XPATH"):
        self.webpage_check()
        alpha = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((getattr(By, locator), value)))
        self.action.move_to_element(alpha).perform()
        time.sleep(0.3)
        text=alpha.text
        return text
    
    def logger(self):
       with open("tvs_invoice_log.txt", "a") as log_file:
        # Write the current time and date to the file
        now = datetime.now()
        log_file.write("\n")
        log_file.write(f"Time of error: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        # Append the traceback to the file
        traceback.print_exc(file=log_file)

    def surf(self):
        pass


    def test_automation(self):
        self.surf()
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    Surfing.main()