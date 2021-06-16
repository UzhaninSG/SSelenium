from selenium import webdriver
from selenium.webdriver.common.by import By
import time

list=['Uzhanin','Stas','UzhaninSG@gmail.com']

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    # Для поиска будем использовать XPath селектор
    element0 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
    element0.send_keys(list[0])
    element1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
    element1.send_keys(list[1])
    element2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
    element2.send_keys(list[2])
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()