#！/user/bin/python
# _*_ coding:UTF-8 _*_
# author:jack
#打开网页

def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()
#登录
def login_fun(driver,username,passdword):
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(passdword)
    driver.find_element_by_id("btnSubmit").click()
#搜索
def search(driver,url,username,passdword,key):
    open_url(driver,url)
    login_fun(driver,username,passdword)
    id=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute('id')
    iframe_id=id+'-frame'
    driver.switch_to.frame(iframe_id)
    driver.find_element_by_xpath("//input[@name='searchNumber']").send_keys(key)
    driver.find_element_by_xpath("//span[@class='l-btn-left']/span").click()
    time.sleep(2)
    num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return  num