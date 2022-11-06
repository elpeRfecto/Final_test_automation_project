from selenium.webdriver.common.by import By


class AuthLocators:
    # эти локаторы служат для переключения с помощью чего выполнить вход (placeholder'ы)
    AUTH_PHONE = (By.ID, 't-btn-tab-phone')
    AUTH_EMAIL = (By.ID, "t-btn-tab-mail")
    AUTH_LOGIN = (By.ID, 't-btn-tab-login')
    AUTH_PASS = (By.ID, "pass")
    AUTH_BANK_BOOK = (By.ID, 't-btn-tab-ls')

    # кнопнки входа и регистрации
    AUTH_BTN = (By.ID, "kc-login")
    REGISTER = (By.ID, 'kc-register')
    REGISTER_BTN = (By.NAME, 'register')
    FORGOT_PASSWORD_BTN = (By.ID, 'forgot_password')
    BACK_BTN = (By.ID, 'reset-back')
    BTN_CONTINUE = (By.ID, 'reset')

    # поля для ввода соответствующие способу входа
    PHONE_FIELD = (By.XPATH, '//*[@id="username"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="username"]')
    LOGIN_FIELD = (By.XPATH, '/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]')
    BANK_BOOK_FIELD = (By.XPATH, '//*[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')

    CAPTCHA = (By.CLASS_NAME, 'rt-captcha__image')
