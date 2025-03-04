from selenium.webdriver.common.by import By


first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
confirm_password_loc = (By.ID, 'password-confirmation')
create_button_loc = (By.CLASS_NAME, 'submit')
greet_message_loc = (By.CSS_SELECTOR, ' [data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
header_title_loc = (By.TAG_NAME, 'h1')
check_information_loc = (By.XPATH, '//*[@class="box-content"]/p')
error_different_password_loc = (By.CSS_SELECTOR, '[id="password-confirmation-error"]')
error_empty_first_name_loc = (By.ID, 'firstname-error')
error_empty_last_name_loc = (By.ID, 'lastname-error')
error_empty_email_loc = (By.ID, 'email_address-error')
error_empty_password_loc = (By.ID, 'password-error')
error_empty_confirm_password_loc = (By.ID, 'password-confirmation-error')
