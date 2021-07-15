# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:38:29 2021

@author: Robpr
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def scrapeTheBOJ(fromYear="2016", toYear="2021", noHeader=True):
    
    pathToDriver = r"C:\Users\Robpr\OneDrive\Documents\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=pathToDriver)
    driver.get("https://www.stat-search.boj.or.jp/ssi/cgi-bin/famecgi2?cgi=$nme_a000_en&lstSelection=PR01")
    
    # Select data
    cpi2015selection = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]")
    ActionChains(driver).move_to_element(cpi2015selection).perform()
    ActionChains(driver).double_click(cpi2015selection).perform()

    ppiSelection = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/div[1]/div[1]/div[1]/table/tbody/tr[1]")
    ActionChains(driver).move_to_element(ppiSelection).perform()
    ActionChains(driver).double_click(ppiSelection).perform()
    
    icommSelection = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/div[1]/div[1]/div[1]/table/tbody/tr[18]")
    ActionChains(driver).move_to_element(icommSelection).perform()
    ActionChains(driver).double_click(icommSelection).perform()
    
    time.sleep(3)
    
    checkAllBox = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[1]/label")
    checkAllBox.click()
    
    # Submit selection
    addButton = driver.find_element_by_xpath("/html/body/div[2]/div/ul[2]/li[1]/div[1]/div[2]/div[4]/a")
    addButton.click()
    
    # Select year range
    fromYearInput = driver.find_element_by_xpath("//*[@id='fromYear']")
    toYearInput = driver.find_element_by_xpath("//*[@id='toYear']")
    fromYearInput.send_keys(fromYear)
    toYearInput.send_keys(toYear)
    
    searchButton = driver.find_element_by_xpath("//*[@id='resultArea']/div[4]/div[1]/a[1]")
    searchButton.click()
    
    driver.switch_to.window(driver.window_handles[1])

    if noHeader==True:
        noHeaderButton = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/label[3]")
        noHeaderButton.click()
    
    downloadButton = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/table/tbody/tr[2]/td[4]/a")
    downloadButton.click()
    
    driver.switch_to.window(driver.window_handles[2])
    downloadLink = driver.find_element_by_xpath("/html/body/div[2]/div/div/center/div/table/tbody/tr/td/a")
    downloadLink.click()
    