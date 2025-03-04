def test_add_to_cart(create_eco_friendly_page):
    create_eco_friendly_page.open_page()  # открываем страницу
    create_eco_friendly_page.check_page_header_title_is('Eco Friendly')  # проверяем заголовок страницы
    item_name = create_eco_friendly_page.choose_item()  # выбираем размер, цвет товара и запоминаем его название
    create_eco_friendly_page.open_cart()  # переходим в корзину
    create_eco_friendly_page.check_page_header_title_is('Shopping Cart')  # проверяем заголвок страницы
    create_eco_friendly_page.check_item_in_cart(item_name)  # сравниваем имя товара в корзине и сохраненное


def test_remove_item_from_cart(create_eco_friendly_page):
    create_eco_friendly_page.open_page()  # открываем страницу
    create_eco_friendly_page.check_page_header_title_is('Eco Friendly')  # проверяем заголовок страницы
    item_name = create_eco_friendly_page.choose_item()  # выбираем размер, цвет товара и запоминаем его название
    create_eco_friendly_page.open_cart_icon()  # открываем корзину через иконку
    create_eco_friendly_page.check_item_in_cart_icon(item_name)  # сравниваем имя товара в корзине и сохраненное
    create_eco_friendly_page.remove_item()  # удаляем товар из корзины
    create_eco_friendly_page.approve_alert()  # подтверждаем удаление товара


def test_sort_by_price(create_eco_friendly_page):
    create_eco_friendly_page.open_page()  # открываем страницу
    create_eco_friendly_page.check_page_header_title_is('Eco Friendly')  # проверяем заголовок страницы
    create_eco_friendly_page.select_sort() # выбираем сортировку по цене
    create_eco_friendly_page.check_sort()  # проверяем что сортировка применилась
