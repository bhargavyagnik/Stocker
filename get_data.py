import pyautogui
from selenium import webdriver
import os
import re
import time
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from html_table_extractor.extractor import Extractor



chromedriver = "D:/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

def goto(url):
    driver.get(url)
    time.sleep(1.5)

def get_stockdata(stock_name):
    goto('https://www.bseindia.com/markets/equity/EQReports/StockPrcHistori.aspx?flag=0')
    username = driver.find_element_by_name("ctl00$ContentPlaceHolder1$smartSearch")
    username.send_keys(stock_name)
    time.sleep(1)
    start_date = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtFromDate")
    start_date.send_keys("05/04/2020")
    start_date = driver.find_element_by_name("ctl00$ContentPlaceHolder1$txtToDate")
    start_date.send_keys("10/04/2020")
    submit=driver.find_element_by_name("ctl00$ContentPlaceHolder1$btnSubmit")
    submit.click()
    time.sleep(1)
    table=driver.find_element_by_name("ContentPlaceHolder1_divStkData")
    print(table)



if(__name__=='__main__'):
    get_stockdata("RELIANCE INDUSTRIES LTD.")


