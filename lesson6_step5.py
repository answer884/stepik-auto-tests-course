import math
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By  

link1 = ("http://suninjuly.github.io/find_link_text")

try:
	browser = webdriver.Chrome()
	browser.get(link1)
	findtext = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
	findtext.click()
	input1 = browser.find_element_by_name("first_name")
	input1.send_keys("Roman")
	input2 = browser.find_element_by_css_selector("[name='last_name']")
	input2.send_keys("Pasechnyi")
	input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.city")
	input3.send_keys("Kyiv")
	input4 = browser.find_element(By.ID, "country")
	input4.send_keys("Ukarine")
	button1 = browser.find_element_by_css_selector(".btn.btn-default")
	button1.click()

finally:
	time.sleep(20)
	browser.quit()