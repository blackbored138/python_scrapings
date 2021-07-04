from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os 
import urllib.request





url = "https://profitable.vip/#/login"
url2 = "https://profitable.vip/#/win"
url3 = "https://www.google.com"
userName = "9495583626"
passWord = "2273626"


browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(url)

time.sleep(1)


username_typebox = browser.find_element_by_xpath("//input[@type='text']")
password_typebox = browser.find_element_by_xpath("//input[@type='password']")
#login_btn = browser.find_element_by_xpath("//button[@class='login_btn']")

username_typebox.send_keys(userName)
password_typebox.send_keys(passWord)
time.sleep(1)

browser.find_element_by_class_name('login_btn').click()


time.sleep(2)

length_li = 0
while length_li < 17:
    li_elements = browser.find_elements_by_tag_name('li')
    length_li = len(li_elements)

time.sleep(10)

browser.get(url2)
print("Program win start")



time.sleep(6)

available_balance = 100
#exit()
while available_balance > 50:

    last_period_len = 0
    while last_period_len == 0:
        last_period = browser.find_elements_by_css_selector('.timenum')
        last_period_len = len(last_period)
 
    current_period_len = 0
    while current_period_len == 0:
        current_period = browser.find_elements_by_css_selector('.bot_ol')
        current_period_len = len(current_period)

    previous_period = 0
    previous_period_color = 'green'
    while previous_period == 0:
        previous_period = browser.find_elements_by_xpath('//table/tbody/tr[1]/td')[0].text
        previous_period_number = browser.find_elements_by_xpath('//table/tbody/tr[1]/td')[2].text

        if int(previous_period_number) % 2 == 0:
            previous_period_color = 'red'
        else:
            previous_period_color = 'green'    



    while last_period_len == 0 or current_period_len == 0:
        continue

    count_down = browser.find_elements_by_css_selector('.van-count-down .span')
    #print("Counts")
    #print(len(count_down))
    #print(count_down[0].text)
    #print(count_down[1].text)
    #print(count_down[2].text)
    #print(count_down[3].text)
    
    #print("Current Period")
    #print(current_period[0].text)
        
    #print("Last Period")
    #print(last_period[0].text)
    #exit()

    if current_period[0].text == '':
        continue 
    
    if count_down[1].text == '':
        continue
    if int(count_down[1].text) >= 1:
        print("Checking Bet")

    if previous_period_color == 'red':
        print("Making Bet")
        join_green = browser.find_element_by_class_name('back_one')
        join_green.click()

        time.sleep(6)


        plus_number_input = browser.find_element_by_class_name('van-stepper__plus')
        #plus_number_input.click()

        #browser.find_elements_by_xpath("//*[contains(text(), 'CONFIRM')]")[0].click()
        print("Made Bet")
        #available_balance = available_balance - 10
        
        browser.find_elements_by_xpath("//*[contains(text(), 'CANCEL')]")[0].click()
        time.sleep(2)
        #break


print("Program ended")


