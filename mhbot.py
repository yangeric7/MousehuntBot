from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time, random

#insert mousehunt credentials here
LOGIN_USERNAME = ''
LOGIN_PASSWORD = ''

def create_page():
	chrome_options = Options()
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument("--start-maximized")

	driver = webdriver.Chrome(chrome_options = chrome_options)
	driver.get("https://www.mousehuntgame.com")
	return driver

def login(driver):
	username = driver.find_element_by_name('accountName')
	username.send_keys(LOGIN_USERNAME)
	password = driver.find_element_by_name('password')
	password.send_keys(LOGIN_PASSWORD)
	remember = driver.find_element_by_name('remember')
	remember.click()
	login = driver.find_element_by_name('doLogin')
	login.click()

def soundHorn(driver):
	horn = driver.find_element_by_class_name('mousehuntHud-huntersHorn')
	horn.click()

#def kingsReward(driver):
def createVariableDelay():
	delay = random.randint(910, 1140)
	return delay

if __name__ == '__main__':
	driver = create_page()

	if driver.current_url == 'https://www.mousehuntgame.com/login.php':
		login(driver)
		time.sleep(2)

	while True:
		soundHorn(driver)
		print "Sounding the Horn!"
		delay = createVariableDelay()
		time.sleep(delay)

	driver.close()