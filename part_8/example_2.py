import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Створюємо об'єкт webdriver для Google Chrome
service = Service(executable_path=r'C:\Users\user\PycharmProjects\chromedriver.exe')
driver = webdriver.Chrome(service=service)
# Відкриваємо веб-сторінку Bing
driver.get("https://www.bing.com")
time.sleep(1)  # Потрібно дочекатися формування сторінки

# Знаходимо поле пошуку за ідентифікатором
search_box = driver.find_element_by_id("sb_form_q")

# Вводимо запит "selenium python" в поле пошуку
search_box.send_keys("selenium python")

# Натискаємо кнопку пошуку за іменем
search_button = driver.find_element_by_name("go")
search_button.click()
# Пауза, щоб побачити результати пошуку
time.sleep(3)

# Закриваємо браузер
driver.quit()
