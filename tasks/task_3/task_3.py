from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def ya_authorization(login, password):
    url = "https://passport.yandex.ru/auth"
    print('Start')
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(url=url)

    login_input = driver.find_element(By.ID, "passp-field-login")
    login_input.clear()
    login_input.send_keys(login)
    sign_in_button_id = 'passp:sign-in'  # passp:sign-in
    driver.find_element(By.ID, sign_in_button_id).click()
    sleep(3)
    password_input = driver.find_element(By.ID, "passp-field-passwd")
    password_input.clear()
    password_input.send_keys(password)
    driver.find_element(By.ID, sign_in_button_id).click()

    sleep(5)
    result = driver.current_url
    driver.close()
    print('End')
    return result
