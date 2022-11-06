from urllib.parse import urlparse
from selenium.webdriver.common.by import By
from conftest import url, password, email, first_name, last_name, login, phone_number, bank_book
from locators import AuthLocators
import random


class BasePage(object):
    # инициализация драйвера
    def __init__(self, driver):
        self.driver = driver

    def visit_page_ros_tel(self):
        # переход по ссылке
        self.driver.get(url)

    def account_link(self):
        accaunt_lk = urlparse(self.driver.current_url)
        return accaunt_lk.path

    """функции для проверки открытия страницы и проверки на ней элементов"""

    def visible_elements_of_phone(self):
        return self.driver.find_element(*AuthLocators.AUTH_PHONE).text

    def visible_elements_of_mail(self):
        return self.driver.find_element(*AuthLocators.AUTH_EMAIL).text

    def visible_elements_of_login(self):
        return self.driver.find_element(*AuthLocators.AUTH_LOGIN).text

    def visible_elements_of_bank_book(self):
        return self.driver.find_element(*AuthLocators.AUTH_BANK_BOOK).text

    # функция для нажатия по кнопке регистрации
    def registration_link_click(self):
        return self.driver.find_element(*AuthLocators.REGISTER).click()

    # функция для ввода имени
    def registration_link_input_name(self):
        return self.driver.find_element(By.NAME, 'firstName').send_keys(first_name)

    # функция для ввода фамилии
    def registration_link_input_last_name(self):
        return self.driver.find_element(By.NAME, 'lastName').send_keys(last_name)

    # функция для ввода электронной почты
    def registration_link_input_email(self):
        return self.driver.find_element(By.ID, "address").send_keys(email)

    # функция для генерации пароля менее 8 символов
    def registration_link_input_password_less_eight_characters(self):
        return self.driver.find_element(By.ID, "password").send_keys(random.randint(1, 100_000))

    # функция для генерации пароля менее 8 символов
    def registration_link_input_conf_password_less_eight_characters(self):
        return self.driver.find_element(By.ID, "password-confirm").send_keys(random.randint(1, 100_000))

    # функция для нажатия по кнопке "зарегистрироваться"
    def registration_button_click(self):
        return self.driver.find_element(*AuthLocators.REGISTER_BTN).click()

    # функция для проверки, что в тесте отсутсвует хотя бы одна заглавная буква
    def error_register_button_of_big_letter(self):
        return self.driver.find_element(By.XPATH,
                                        '/html/body/div[1]/main/section[2]/div/div/div/form/div[4]/div[1]/span').text

    # функция для проверки, что в тесте меньше 8 символов
    def error_register_button_of_eight_symbols(self):
        return self.driver.find_element(By.XPATH,
                                        '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text

    # функция для генерации пароля более 8 символов без букв
    def registration_link_input_password_more_eight_characters_without_capital_letter(self):
        return self.driver.find_element(By.ID, "password").send_keys(random.randint(100_000_000, 100_000_000_000_000))

    # функция для генерации пароля более 8 символов без букв
    def registration_link_input_conf_password_more_eight_characters_without_capital_letter(self):
        return self.driver.find_element(By.ID, "password-confirm").send_keys(random.randint(100_000_000, 100_000_000_000_000))

    # функция для проверки на несовпадение пароля
    def registration_link_input_password_pass_do_not_match(self):
        return self.driver.find_element(By.ID, "password").send_keys('Qwerty123')

    # функция для проверки на несовпадение пароля для поля подтверждение пароля
    def registration_link_input_conf_password_pass_do_not_match(self):
        return self.driver.find_element(By.ID, "password-confirm").send_keys('Qwerty321')

    def registration_link_password_do_not_match(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span').text

    # функция для ввода пароля при попытке зарегистрироваться
    def registration_link_input_password(self):
        return self.driver.find_element(By.ID, "password").send_keys(password)

    # функция для повторного ввода пародля при попытке зарегистрироваться
    def registration_link_input_password_confirm(self):
        return self.driver.find_element(By.ID, "password-confirm").send_keys(password)

    # функция для проверки входа в ЛК
    def registration_link_confirm_email_with_code(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/h1[1]').text

    # функция для проверки, зарегистрирован ли такой пользователь
    def registration_link_email_account_already_exists(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2').text

    # кликает на placeholder email
    def try_email_auth(self):
        return self.driver.find_element(*AuthLocators.AUTH_EMAIL).click()

    # функция кликает в поле ввода электронной почты
    def try_email_auth_field_input(self):
        return self.driver.find_element(*AuthLocators.EMAIL_FIELD).click()

    # функция заполняет данными поля для ввода электронной почты
    def try_email_input_data(self):
        return self.driver.find_element(*AuthLocators.EMAIL_FIELD).send_keys(email)

    # кликает по полю для ввода пароля
    def try_password_auth_field_input(self):
        return self.driver.find_element(*AuthLocators.PASSWORD_FIELD).click()

    # вводит пароль
    def try_auth_pass_input(self):
        return self.driver.find_element(*AuthLocators.PASSWORD_FIELD).send_keys(password)

    # нажимает на кнопку "войти"
    def try_press_btn_enter(self):
        return self.driver.find_element(*AuthLocators.AUTH_BTN).click()

    # кликает на placeholder логина
    def try_login_auth(self):
        return self.driver.find_element(*AuthLocators.AUTH_LOGIN).click()

    # кликает на поле ввода логина
    def try_login_auth_field_input(self):
        return self.driver.find_element(*AuthLocators.LOGIN_FIELD).click()

    # заполняет данные в поле ввода логина
    def try_login_input_data(self):
        return self.driver.find_element(*AuthLocators.LOGIN_FIELD).send_keys(login)

    # кликает на placeholder телефона
    def try_phone_auth(self):
        return self.driver.find_element(*AuthLocators.AUTH_PHONE).click()

    # кликает на поле ввода телефона
    def try_phone_auth_field_input(self):
        return self.driver.find_element(*AuthLocators.PHONE_FIELD).click()

    # заполняет данные в поле ввода телефона
    def try_phone_input_data(self):
        return self.driver.find_element(*AuthLocators.PHONE_FIELD).send_keys(phone_number)

    # сообщение о неверно введённом логине/пароле или текста с картинке
    def wrong_login_or_password(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/p').text

    # кликает на placeholder лицевого счёта
    def try_bank_book_auth(self):
        return self.driver.find_element(*AuthLocators.AUTH_BANK_BOOK).click()

    # кликает на поле ввода лицевого счёта
    def try_bank_book_auth_field_input(self):
        return self.driver.find_element(*AuthLocators.BANK_BOOK_FIELD).click()

    # заполняет данные в поле ввода лицевого счёта
    def try_bank_book_input_data(self):
        return self.driver.find_element(*AuthLocators.BANK_BOOK_FIELD).send_keys(bank_book)

    # надимает на кнопку "забыл пароль"
    def press_btn_forgot_password(self):
        return self.driver.find_element(*AuthLocators.FORGOT_PASSWORD_BTN).click()

    # проверка капчи на странице
    def check_captcha_on_page(self):
        return self.driver.find_element(*AuthLocators.CAPTCHA)

    # нажимает на кнопку назад на странице восстановления пароля
    def press_back_btn_on_page_of_forgot_password(self):
        return self.driver.find_element(*AuthLocators.BACK_BTN).click()

    # нажимает кноку "продолжить" на странице восстановления пароля
    def btn_continue_on_page_forgot_password(self):
        return self.driver.find_element(*AuthLocators.BTN_CONTINUE).click()

    # сообщение о неверном логине или текста с картинке
    def wrong_login_or_text_to_picture(self):
        return self.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/p[1]/').text
