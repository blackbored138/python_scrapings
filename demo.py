from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


url = "https://www.flipkart.com/search?q="
itemName = "Laptops"
url = url + itemName

browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get(url)

variable = 1
while variable > 0:
    items = browser.find_elements_by_class_name("_1AtVbE")
    itemPrice = browser.find_elements_by_class_name("_30jeq3")
    itemName = browser.find_elements_by_class_name("_4rR01T")

    highestPrice = 0
    i = 0
    for content in itemName:
        price = itemPrice[i].text[1:]
        item_name = itemName[i].text
        i += 1
        #print(itemName)
        #break
        price = price.replace(',', '')
        price = int(price)

        if highestPrice < price:
            highestPrice = price

        if 40000 > price:
            print(str(price) + " ----- " + item_name)

    #print("Highest Price is " + str(highestPrice))
    print("Loop "+ str(variable))
    #break   
    if variable > 4:
        break    
    variable += 1
    url2 = url + "&page=" + str(variable)
    browser.get(url2)

print("Program ended")


