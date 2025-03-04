from pages.base_pages import BasePage
from faker import Faker
from pages.locators import create_account_locators as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'


    def fill_form(self, same_password=True):
        fake = Faker()
        first_name_field = self.find(loc.first_name_loc)
        first_name = fake.first_name()
        first_name_field.send_keys(first_name)
        last_name_field = self.find(loc.last_name_loc)
        last_name = fake.last_name()
        last_name_field.send_keys(last_name)
        self.driver.execute_script('window.scrollTo(0, 500)')
        email_field = self.find(loc.email_loc)
        email = fake.email()
        email_field.send_keys(email)
        password_field = self.find(loc.password_loc)
        password = fake.password()
        password_field.send_keys(password)
        confirm_password_field = self.find(loc.confirm_password_loc)
        if same_password:
            confirm_password_field.send_keys(password)
            button = self.find(loc.create_button_loc)
            button.click()
            WebDriverWait(self.driver,5).until(
                EC.text_to_be_present_in_element(
                loc.header_title_loc,
                'My Account'
                )
            )
            return first_name, last_name, email
        else:
            confirm_password_field.send_keys(fake.password())
            button = self.find(loc.create_button_loc)
            button.click()


    def check_registering_message(self, text):
        assert self.find(loc.greet_message_loc).text == text


    def check_account_data(self, first_name, last_name, email):
        actual_text = self.find(loc.check_information_loc).text.strip()
        name_email = actual_text.split("\n")
        actual_name = name_email[0]
        actual_email = name_email[1]
        assert f'{first_name} {last_name}' == actual_name
        assert email == actual_email


    def check_error_different_password(self, text):
        assert self.find(loc.error_different_password_loc).text == text

    def submit_empty_form(self):
        button = self.find(loc.create_button_loc)
        button.click()


    def check_required_field_error(self, text):
        assert self.find(loc.error_empty_first_name_loc).text == text
        assert self.find(loc.error_empty_last_name_loc).text == text
        assert self.find(loc.error_empty_email_loc).text == text
        assert self.find(loc.error_empty_password_loc).text == text
        assert self.find(loc.error_empty_confirm_password_loc).text == text
