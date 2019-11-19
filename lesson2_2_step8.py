from selenium import webdriver
import time
import math
import os


link = "http://suninjuly.github.io/file_input.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("Adele")
    browser.find_element_by_name("lastname").send_keys("Adele")
    browser.find_element_by_name("email").send_keys("Adele")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty.txt')
    browser.find_element_by_name("file").send_keys(file_path)

    button = browser.find_element_by_xpath("/html/body/div/form/button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла