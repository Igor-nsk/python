# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://mail.ru/")
        driver.find_element_by_id("mailbox:login").click()
        driver.find_element_by_id("mailbox:login").click()
        driver.find_element_by_xpath(u"//input[@value='Ввести пароль']").click()
        driver.find_element_by_id("mailbox:password").click()
        driver.find_element_by_id("mailbox:password").clear()
        driver.find_element_by_id("mailbox:password").send_keys("igi1987")
        driver.find_element_by_xpath(u"//input[@value='Ввести пароль']").click()
        driver.find_element_by_id("PH_logoutLink").click()
        driver.find_element_by_xpath("//div[@id='app-canvas']/div/div/div/div/div[2]/div/div/div/div/div/div/span/span/span").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("(//input[@value=''])[12]").click()
        driver.find_element_by_xpath("(//input[@value='pithonich@mail.ru'])[2]").clear()
        driver.find_element_by_xpath("(//input[@value='pithonich@mail.ru'])[2]").send_keys("pithonich@mail.ru")
        driver.find_element_by_name("Subject").click()
        driver.find_element_by_name("Subject").clear()
        driver.find_element_by_name("Subject").send_keys("hello")
        driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
        driver.find_element_by_xpath("//div[5]/div/div/div[2]/div/div/div").click()
        # ERROR: Caught exception [unknown command [editContent]]
        driver.find_element_by_xpath("//div[2]/div/span/span/span").click()
        driver.find_element_by_css_selector("svg.ico.ico_16-close.ico_size_s").click()
        driver.find_element_by_xpath("//div[@id='app-canvas']/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div/div/div/div/a/div[4]/div/div/span").click()
        driver.find_element_by_xpath("//div[@id='app-canvas']/div/div/div/div/div[2]/div/div/div/div/div[2]/div/div/nav/a/div/div[2]/div").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
