from PMOProject.Locators.locators import Locators
class LoginPage:
    def __init__(self, driver):
        self.driver= driver

    def click_login(self):
        self.driver.find_element_by_xpath(Locators.login_btn_xpath).click()

    def enter_mail(self, mailAdresse):
        self.driver.find_element_by_xpath(Locators.mail_textbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.mail_textbox_xpath).send_keys(mailAdresse)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(Locators.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(Locators.password_textbox_xpath).send_keys(password)

    def click_logOn(self):
        self.driver.find_element_by_name(Locators.logIn_btn_name).click()

