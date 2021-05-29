from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os 
import wget 
import urllib.request





url = "https://www.instagram.com/accounts/login/"
url2 = "http://www.smsmartcatechism.org/files/media/classes/"
userName = "peacefullclicker"
#url2 = url2 + userName


browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(url2)

variable = 1
while variable > 0:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    variable += 1
    if variable == 3:
        break 


images = browser.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
path = os.getcwd()
path = os.path.join(path,userName)




os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, userName + str(counter) + '.jpg')
    urllib.request.urlretrieve(image, save_as)
    counter += 1
    #print("Images saving number " + str(counter))




print("Program ended")


