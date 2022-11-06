import time
import pytest
from base_page import BasePage
from conftest import captcha
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(15)
    yield driver
    driver.set_page_load_timeout(15)
    driver.implicitly_wait(15)
    driver.quit()


def test_open_ros_tel_site(driver):
    """"проверка на открытие страницы и присутствие на ней элементов"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    assert ros_tel_page.visible_elements_of_phone() == 'Телефон'
    assert ros_tel_page.visible_elements_of_mail() == 'Почта'
    driver.implicitly_wait(5)
    assert ros_tel_page.visible_elements_of_login() == 'Логин'
    assert ros_tel_page.visible_elements_of_bank_book() == 'Лицевой счёт'


def test_registration_link_less_eight_characters_password_error(driver):
    """переход по кнопке регистрации и ввод данных, где длина пароля генерируется случайно,
    но меньше 8 цифр"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.registration_link_click()
    ros_tel_page.registration_link_input_name()
    ros_tel_page.registration_link_input_last_name()
    ros_tel_page.registration_link_input_email()
    ros_tel_page.registration_link_input_password_less_eight_characters()
    ros_tel_page.registration_link_input_conf_password_less_eight_characters()
    ros_tel_page.registration_button_click()
    assert ros_tel_page.error_register_button_of_eight_symbols() == 'Длина пароля должна быть не менее 8 символов'


def test_registration_link_must_contain_one_capital_letter(driver):
    """переход по кнопке регистрации и ввод данных, где длина пароля генирируется случайно,
    но больше 8 символов и нет ни одной заглавной буквы"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.registration_link_click()
    ros_tel_page.registration_link_input_name()
    ros_tel_page.registration_link_input_last_name()
    ros_tel_page.registration_link_input_email()
    ros_tel_page.registration_link_input_password_more_eight_characters_without_capital_letter()
    ros_tel_page.registration_link_input_conf_password_more_eight_characters_without_capital_letter()
    ros_tel_page.registration_button_click()
    assert ros_tel_page.error_register_button_of_eight_symbols() == 'Пароль должен содержать хотя бы одну заглавную букву'


def test_registration_link_password_do_not_match(driver):
    """переход по кнопке регистрации и ввод данных, где пароли не совпадают"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.registration_link_click()
    ros_tel_page.registration_link_input_name()
    ros_tel_page.registration_link_input_last_name()
    ros_tel_page.registration_link_input_email()
    ros_tel_page.registration_link_input_password_pass_do_not_match()
    ros_tel_page.registration_link_input_conf_password_pass_do_not_match()
    ros_tel_page.registration_button_click()
    assert ros_tel_page.registration_link_password_do_not_match() == 'Пароли не совпадают'


def test_registration_link_try_registration(driver):
    """прохождение регистрации до момента, где нужно подтверждение пароля с электронной почты или
    проверки, что учётная запись с такимим данными уже существует"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.registration_link_click()
    ros_tel_page.registration_link_input_name()
    ros_tel_page.registration_link_input_last_name()
    ros_tel_page.registration_link_input_email()
    ros_tel_page.registration_link_input_password()
    ros_tel_page.registration_link_input_password_confirm()
    ros_tel_page.registration_button_click()
    try:
        assert ros_tel_page.registration_link_confirm_email_with_code() == 'Подтверждение email'
    except:
        assert ros_tel_page.registration_link_email_account_already_exists() == 'Учётная запись уже существует'


def test_email_enter(driver):
    """авторизация по электронной почте и проверкой входа в ЛК"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.try_email_auth()
    ros_tel_page.try_email_auth_field_input()
    ros_tel_page.try_email_input_data()
    ros_tel_page.try_password_auth_field_input()
    ros_tel_page.try_auth_pass_input()
    ros_tel_page.try_press_btn_enter()
    time.sleep(5)
    assert ros_tel_page.account_link() == '/account_b2c/page'


def test_login_enter(driver):
    """авторизация по логину и проверкой входа в ЛК"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.try_login_auth()
    ros_tel_page.try_login_auth_field_input()
    ros_tel_page.try_login_input_data()
    ros_tel_page.try_password_auth_field_input()
    ros_tel_page.try_auth_pass_input()
    ros_tel_page.try_press_btn_enter()
    time.sleep(5)
    assert ros_tel_page.account_link() == '/account_b2c/page'


def test_phone_enter(driver):
    """проба авторизации по телефону, но так как телефон не указан в ЛК, то ожидаем ошибку входа"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.try_phone_auth()
    ros_tel_page.try_phone_auth_field_input()
    ros_tel_page.try_phone_input_data()
    ros_tel_page.try_password_auth_field_input()
    ros_tel_page.try_auth_pass_input()
    ros_tel_page.try_press_btn_enter()
    try:
        assert ros_tel_page.wrong_login_or_password() == 'Неверный логин или пароль'
    except:
        assert ros_tel_page.wrong_login_or_password() == 'Неверно введен текст с картинки'


def test_bank_book_enter(driver):
    """проба авторизации по лицевому счёту, но так как лицевой счёт не указан в ЛК, то ожидаем ошибку входа"""
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.try_bank_book_auth()
    ros_tel_page.try_bank_book_auth_field_input()
    ros_tel_page.try_bank_book_input_data()
    ros_tel_page.try_password_auth_field_input()
    ros_tel_page.try_auth_pass_input()
    ros_tel_page.try_press_btn_enter()
    try:
        assert ros_tel_page.wrong_login_or_password() == 'Неверный логин или пароль'
    except:
        assert ros_tel_page.wrong_login_or_password() == 'Неверно введен текст с картинки'


def test_captcha_on_page_forgot_password(driver):
    """переход по ссылке "забыл пароль", там мы смотрим, если есть капча,
    то пробуем восстановить пароль по электронной почте, если не получается - жмем по кнопке "вернуться назад" """
    ros_tel_page = BasePage(driver)
    ros_tel_page.visit_page_ros_tel()
    ros_tel_page.press_btn_forgot_password()
    ros_tel_page.try_email_auth()
    ros_tel_page.try_email_auth_field_input()
    ros_tel_page.try_email_input_data()
    time.sleep(2)
    if 'src' in captcha:
        try:
            ros_tel_page.btn_continue_on_page_forgot_password()
        except:
            ros_tel_page.press_back_btn_on_page_of_forgot_password()
            assert ros_tel_page.wrong_login_or_text_to_picture() == ' Неверный логин или текст с картинки'
