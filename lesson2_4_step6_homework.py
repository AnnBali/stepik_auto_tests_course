from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver



browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.get("http://suninjuly.github.io/wait2.html")

try: 
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "verify"))
        )
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
        
# предупреждение и текст ошибки в тесте при провале
except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:

    # закрываем браузер после всех манипуляций
    browser.quit()

