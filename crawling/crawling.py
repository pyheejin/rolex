import time
import csv
from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
link = driver.get("https://www.rolex.com/ko/watches/configure.html#/day-date/m128238-0045/dial")
time.sleep(2)

dials = driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div[6]/div[1]/div/div[1]/div[1]/div/div/div[1]/ul')

for i in dials:
    print(i.find_element_by_xpath('/picture/source').get_attribute('srcset'))