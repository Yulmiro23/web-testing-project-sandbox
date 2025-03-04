from selenium.webdriver.common.by import By

picture_loc = (By.CSS_SELECTOR, '[src="https://magento.softwaretestingboard.com/pub/media/wysiwyg/sale/sale-main.jpg"]')
text_loc = (By.XPATH, "//strong[@class='title' and text()=\"You can't have too many tees\"]")
menu_point = (By.XPATH, "//strong[@class='title']/span[text()=\"Women's Deals\"]"
                        "/ancestor::div[@class=\"categories-menu\"]//a[text()=\"Hoodies and Sweatshirts\"]")
section_loc = (By.ID, 'ui-id-4')
