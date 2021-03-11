from PMOProject.Locators.locators import Locators

class PracticePage :


 def __init__(self, driver):
    self.driver = driver


 def click_Radio_Button_benz (self):
    self.driver.find_element_by_xpath(Locators.radio_btn_benz_xpath).click()
 def click_selekt_Button_benz (self):
    self.driver.find_element_by_xpath(Locators.select_value_benz_xpath).click()
 def click_color_orange(self):
    self.driver.find_element_by_xpath(Locators.select_color_orange_xpath).click()
 def click_chekBox_benz (self):
    self.driver.find_element_by_xpath(Locators.select_checkbox_orange_xpath).click()

