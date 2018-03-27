"""
Googleでtextと検索するプログラム
"""


from selenium import webdriver
import webbrowser

driver = webdriver.Chrome()
driver.get("https://www.google.co.jp/?gfe_rd=cr&dcr=0&ei=le65WqrLFaquX9-pqMAI")

driver.find_element_by_name('q').send_keys("text")
driver.find_element_by_name('btnK').click()

webbrowser.open("https://master.tech-camp.in/admin/chat_messages")
webbrowser.open("https://calendar.google.com/calendar/r")


driver.close()
driver.quit()
