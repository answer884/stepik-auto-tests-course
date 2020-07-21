from selenium import webdriver
from selenium.webdriver.common.by import By 
import time 

link1 = ("http://suninjuly.github.io/registration2.html")

try:
	browser = webdriver.Chrome()
	browser.get(link1)
	input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
	input1.send_keys("Roman")
	input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
	input2.send_keys('Roman')
	input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
	input3.send_keys("roman@gmail.com")
	button1 = browser.find_element_by_class_name("btn.btn-default")
	button1.click()
	time.sleep(1)

	welcome_text_elt = browser.find_element_by_tag_name("h1")
	welcome_text = welcome_text_elt.text
	assert "Congratulations!You have successfully registered!" == welcome_text

finally:
	time.sleep(10)
	browser.quit()



