from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id("num1")
    y = browser.find_element_by_id("num2")
    ans = str(int(x.text)+int(y.text))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(ans)

    button = browser.find_element_by_xpath("/html/body/div/form/button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла