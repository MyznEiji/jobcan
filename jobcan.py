"""
Googleでtextと検索するプログラム
"""
from selenium import webdriver

file = open('myPass.txt', 'r')
myPassList = file.read().split(',')
email = myPassList[0]
myPass = myPassList[1]


driver = webdriver.Chrome()
driver.get("https://ssl.jobcan.jp/login/pc-employee/?client_id=&code=&url=https%3A%2F%2Fssl.jobcan.jp%2Femployee")

driver.find_element_by_name('client_id').send_keys("div")
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(myPass)

driver.find_element_by_id('adit-button-work-start').click()

# driver.close()
# driver.quit()
