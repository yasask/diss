import time
import csv
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


pd.read_csv('1million_url_list.csv')

with open('million_url_list_v2.csv', 'rb') as f:
    readCSV = csv.reader(f)
    url_list = map(tuple, readCSV)
    for row in readCSV:
        url_list.append(row)

def stringTrunc(tuple):
    string = tuple[0]
    return string

test = stringTrunc(url_list[0])
test1 = test.lstrip()
print test.rstrip()
print(test1)
print("http://" + stringTrunc(url_list[2]))
print("http://" + stringTrunc(url_list[0]))
driver = webdriver.Chrome(executable_path='/Users/Yasas/Desktop/chromedriver')



for x in url_list:
    driver.get('http://' + stringTrunc(x))
    time.sleep(0.1)
driver.close()
