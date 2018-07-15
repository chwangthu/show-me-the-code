#!usr/bin/env python3
#-*- coding:utf-8 -*-
'''
Learned:
    1. Add chormedriver to path
    2. alert accept
    3. find element
Unsolved:
    alert window cannot close
    xpath cannot locate
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.action_chains import ActionChains
import time

def login_in():
    driver = webdriver.Chrome()  
    driver.get("http://www.hfjyyun.net.cn/App.ResourceCloud/")
    driver.switch_to_alert().accept()

    elem_user = driver.find_element_by_name("username")
    elem_user.clear
    elem_user.send_keys("xxx")  
    elem_pwd = driver.find_element_by_name("password")
    elem_pwd.clear
    elem_pwd.send_keys("xxx")  
    elem_pwd.send_keys(Keys.RETURN) # enter key

    #driver.find_element_by_id("loginBtn").click()
    #driver.find_element_by_id("loginBtn").submit()
    #time.sleep(5) 

    return driver

if __name__ == "__main__":
    driver = login_in()
    time.sleep(10)
    # element = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath('//*[@id="index-login-box"]/div/div/div/a[1]')).is_displayed
    ele = driver.find_element_by_xpath('//*[@id="glfw"]/a')
    # move the mouse
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="glfw"]/ul/li[3]/a').click()

    #time.sleep(10)
    #print("wait finished")
    #driver.switch_to_window(driver.window_handles[0]).send_keys(Keys.RETURN)
    # alert = driver.switch_to_frame()
    # print(alert)
    # print(alert.text)
    # alert.accept()
    # print("alert finished")
    # driver.find_element_by_xpath('//*[@id="fix_header"]/div/div/div[1]/ul/li[1]/a').click()
    # #driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[2]/div[2]/ul/li[1]/a/div').click()

    # time.sleep(5)
    # driver.switch_to_alert().accept()
    # driver.find_element_by_xpath('/html/body/div[3]/div[4]/div[2]/div[2]/div[3]/div[2]/ul/li/div/div/div/img[5]').click()


    driver.close()  
    driver.quit() 