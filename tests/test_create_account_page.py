def test_create_account(create_acc_page):
    create_acc_page.open_page()  # открываем страницу
    create_acc_page.check_page_header_title_is('Create New Customer Account')  # проверяем заголовок страницы
    first_name, last_name, email = create_acc_page.fill_form(same_password=True)  # заполняем форму, поля password и confirm password совпадают
    create_acc_page.check_registering_message('Thank you for registering with Main Website Store.')  # проверяем информациооное сообщение
    create_acc_page.check_account_data(first_name, last_name, email)  # cравниваем сохраненные данные и те, что на странице информации


def test_different_password(create_acc_page):
    create_acc_page.open_page()  # открываем страницу
    create_acc_page.check_page_header_title_is('Create New Customer Account')  # проверяем заголовок страницы
    create_acc_page.fill_form(same_password=False)  # заполняем форму, поля password и confirm password не совпадают
    create_acc_page.check_error_different_password('Please enter the same value again.') # проверяем сообщение об ошибке


def test_required_fields(create_acc_page):
    create_acc_page.open_page()  # открываем страницу
    create_acc_page.check_page_header_title_is('Create New Customer Account')  # проверяем заголовок страницы
    create_acc_page.submit_empty_form()  # отрправляем пустую форму
    create_acc_page.check_required_field_error('This is a required field.')  # проверяем, что на всех полях появилось сообщение об ошибке
