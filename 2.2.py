
import time 
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    btn = browser.find_element_by_css_selector("button.btn-primary")
    btn.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()
    
finally:
    
    time.sleep(20)
        # закрываем браузер после всех манипуляций
    browser.quit()
    