from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name("btn-primary").click()
    browser.switch_to.alert.accept()
    x = browser.find_element_by_id("input_value")
    x = x.text
    x = calc(x)
    browser.find_element_by_id("answer").send_keys(x)
    browser.find_element_by_class_name("btn-primary").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла