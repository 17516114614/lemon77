#！/user/bin/python
# _*_ coding:UTF-8 _*_
# author:jack
from common import  code
from  test_data import  data
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
import time
url=data.dict.get('url')
code.open_url(driver,url)
