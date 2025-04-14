from pages.base_pages import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'


    def choose_item(self):
        self.driver.execute_script('window.scrollTo(0, 500)')
        cards = self.find_all(loc.cards_loc)
        card = cards[0]
        name = self.find(loc.name_item_loc).text
        colour = self.find(loc.color_loc)
        size = self.find(loc.size_loc)
        button = self.find(loc.button_cart_loc)
        ActionChains(self.driver).move_to_element(card).click(colour).click(size).click(button).perform()
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                loc.message_successful_added_loc,
                f'You added {name} to your shopping cart.'
            )
        )
        self.driver.execute_script('window.scrollTo(0, 0)')
        return name


    def open_cart(self):
        cart_link = self.find(loc.cart_loc)
        cart_link.click()


    def check_item_in_cart(self, name):
        assert self.find(loc.name_in_cart_loc).text == name


    def open_cart_icon(self):
        button_cart = self.find(loc.cart_icon_loc)
        button_cart.click()


    def check_item_in_cart_icon(self, name):
        self.driver.implicitly_wait(5)
        assert self.find(loc.cart_icon_item_name_loc).text == name


    def remove_item(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc.remove_icon_loc))
        remove_icon = self.find(loc.remove_icon_loc)
        remove_icon.click()


    def approve_alert(self):
        ok_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(loc.alert_accept_loc)
        )
        ok_button.click()
        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element(
                loc.inform_message_loc,
                'You have no items in your shopping cart.'
            )
        )


    def select_sort(self):
        select_sort = self.find(loc.select_sort_loc)
        dropdown_sort = Select(select_sort)
        dropdown_sort.select_by_value('price')
        sleep(5)
        new_url = self.driver.current_url
        print(new_url)
        # WebDriverWait(self.driver, 10).until(
        #     EC.url_to_be(
        #         'https://magento.softwaretestingboard.com/collections/eco-friendly.html?product_list_order=price'
        #     )
        # )



    def check_sort(self):
        self.driver.implicitly_wait(10)
        price = self.find_all(loc.price_loc)
        price_start = price[0].text
        price_finish = price[11].text
        price_start = float(price_start[1:])
        price_finish = float(price_finish[1:])
        print(price_finish, price_start)
        assert price_start < price_finish
