def test_open_section_by_picture(create_sale_page):
    create_sale_page.open_page() # открываем страницу
    create_sale_page.check_page_header_title_is('Sale') # проверяем заголовок страницы
    create_sale_page.open_page_in_new_tab() # по клику на картинке+ctrl в соседней вкладке открываем страницу с скидками
    create_sale_page.check_page_header_title_is('Women Sale') # проверяем заголовок открытой страницы


def test_open_section_by_link(create_sale_page):
    create_sale_page.open_page() # открываем страницу
    create_sale_page.check_page_header_title_is('Sale') # проверяем заголовок страницы
    create_sale_page.open_page_in_same_tab() # по клику на ссылку в той же вкладке открывается страница с скидками
    create_sale_page.check_page_header_title_is('Tees') # проверяем заголовок открытой страницы


def test_open_point_in_menu(create_sale_page):
    create_sale_page.open_page() # открываем страницу
    create_sale_page.check_page_header_title_is('Sale') # проверяем заголовок страницы
    create_sale_page.open_point() # открываем пункт 'Hoodies & Sweatshirts' в женском разделе
    create_sale_page.check_page_header_title_is('Hoodies & Sweatshirts') # проверяем заголовок открытой страницы
    create_sale_page.check_correct_section() # проверяем, что страница открылась в женском разделе
