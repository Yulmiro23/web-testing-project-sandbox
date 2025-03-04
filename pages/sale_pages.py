from pages.base_pages import BasePage
from pages.locators import sale_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SalePage(BasePage):
    page_url = '/sale.html'


    def open_page_in_new_tab(self):
        picture = self.find(loc.picture_loc)
        ActionChains(self.driver).key_down(Keys.CONTROL).click(picture).key_up(Keys.CONTROL).perform()
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])


    def open_page_in_same_tab(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        text = self.find(loc.text_loc)
        text.click()


    def open_point(self):
        point = self.find(loc.menu_point)
        point.click()


    def check_correct_section(self):
        assert self.find(loc.section_loc).text == 'Women'
