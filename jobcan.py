"""
Googleでtextと検索するプログラム
"""
from selenium import webdriver
import webbrowser
from termcolor import cprint
import subprocess


# Password関連を参照
file = open('/Users/miyazonoeiji/projects/python/jobcan/myPass.txt', 'r')
myPassList = file.read().split(',')
email = myPassList[0]
myPass = myPassList[1]

#ジョブカン自動出勤
driver = webdriver.Chrome()
driver.get("https://ssl.jobcan.jp/login/pc-employee/?client_id=&code=&url=https%3A%2F%2Fssl.jobcan.jp%2Femployee")

driver.find_element_by_name('client_id').send_keys("div")
driver.find_element_by_name('email').send_keys(email)
driver.find_element_by_name('password').send_keys(myPass)

driver.find_element_by_id('adit-button-work-start').click()


# 入力待ち
cprint("Please press the 'Enteer_Key' as soon as it is confirmed", "yellow")
input_waiting = input()


# 遠隔とグーグルカレンダーを開く
webbrowser.open("https://master.tech-camp.in/admin/chat_messages")
webbrowser.open("https://calendar.google.com/calendar/r")

#  slackを開く
#subprocess.run(["open -a slack"], shell=True)
webbrowser.open("https://di-v.slack.com/messages/C286UJESF/")

# 渋谷現場管理ページ
webbrowser.open("https://master.tech-camp.in/admin/users/classrooms")

driver.close()
driver.quit()
