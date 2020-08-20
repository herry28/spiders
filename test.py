import unittest
import  time
from selenium import webdriver
driver=webdriver.Chrome()
url="http://www.baidu.com"
driver.get(url)
time.sleep(3)
driver.close()

