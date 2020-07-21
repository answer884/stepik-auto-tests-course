from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link1 = ("http://suninjuly.github.io/huge_form.html")

try:
	browser = webdriver.Chrome()
	browser.get(link1)
	elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")

	for element in elements:
		element.send_keys("Мой ответ")

	button1 = browser.find_element_by_css_selector(".btn.btn-default")
	button1.click()


finally:
	
	time.sleep(20)
	browser.quit()