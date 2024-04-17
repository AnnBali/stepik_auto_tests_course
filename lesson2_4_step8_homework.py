from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 25).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button = WebDriverWait(browser, 25).until(
            EC.element_to_be_clickable((By.ID, "book"))
        )
    button.click()
    
    # найти число x. и забрать из него текст   
    x_element = browser.find_element(By.CSS_SELECTOR, 'span[id="input_value"]')
    x = x_element.text
# Посчитать математическую функцию от x.
    y = calc(x)
# Ввести ответ в текстовое поле.
    browser.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys(y)
# Найти и Нажать на кнопку "Submit".
    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

# ловим алерт и забираем из него ответ, который отразится в консоли
    print(browser.switch_to.alert.text.split()[-1])

# предупреждение и текст ошибки в тесте при провале
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

