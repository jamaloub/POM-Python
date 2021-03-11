from selenium import webdriver
import unittest
from PMOProject.Pages.Login import LoginPage
from PMOProject.Pages.PracticePage import PracticePage
import time
import HtmlTestRunner
class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
         self.driver= webdriver.Chrome(executable_path="C:/Users/jamal/PycharmProjects/Test/Drivers/chromedriver.exe")
         self.driver.implicitly_wait(5)
         self.driver.maximize_window()

    def test_01_login(self):
        driver= self.driver
        driver.get("https://letskodeit.teachable.com")

        login= LoginPage(driver)
        login.click_login()
        login.enter_mail("jamal_oubaouih@yahoo.de")
        login.enter_password("12344")
        login.click_logOn()
        time.sleep(2)
        login.driver.close

    def test_02_PracticePage(self):
        driver=self.driver
        driver.get("https://letskodeit.teachable.com/p/practice")

        car= PracticePage(driver)
        car.click_Radio_Button_benz()
        car.click_selekt_Button_benz()
        car.click_color_orange()
        car.click_chekBox_benz()

    @classmethod
    def tearDownClass(self):
          self.driver.close
          self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jamal/PycharmProjects/Test/PMOProject/Reports'))