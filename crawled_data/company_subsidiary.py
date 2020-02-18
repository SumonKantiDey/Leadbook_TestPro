from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from datetime import date, datetime
import json
options = Options()
options.add_argument("--headless")
store_data = []


def _setup():
    chrome_driver = "D:/Leadbook/crawled_data/driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


def _pagination_index(page):
    pagination = f"//*[@id = 'subsidiaryTable_paginate']/span/a[{page}]"
    return pagination


def _click_option():
    option = "//*[@id='subsidiaryTable_length']/label/select/option[4]"
    return option


def _get_row_columns(driver, page):
    rows = len(driver.find_elements_by_xpath(
        ".//*[@id='subsidiaryTable']/tbody/tr"))
    if rows <= 1:
        columns = len(driver.find_elements_by_xpath(
            f".//*[@id='subsidiaryTable']/tbody/tr/td"))
    else:
        columns = len(driver.find_elements_by_xpath(
            f".//*[@id='subsidiaryTable']/tbody/tr[{page}]/td"))
    return rows, columns


def _subsidiary(driver, company_profile):
    dic = {
        1: "name",
        2: "type",
        3: "total asset",
        4: "percentage"
    }
    page_url = "//*[@id='subsidiaryTable_paginate']/span/a"

    subsidiaries = []
    driver = _setup()
    driver.get(company_profile)
    pages = len(driver.find_elements_by_xpath(page_url))

    if pages > 0:
        option_click = _click_option()
        driver.find_elements_by_xpath(option_click)[0].click()
        pages = len(driver.find_elements_by_xpath(page_url))
    time.sleep(5)

    for page in range(1, pages + 1):
        driver = _setup()
        driver.get(company_profile)
        time.sleep(10)
        pagination = _pagination_index(page)
        option_click = _click_option()
        driver.find_elements_by_xpath(option_click)[0].click()
        driver.find_elements_by_xpath(pagination)[0].click()

        rows, columns = _get_row_columns(driver, page)

        for row in range(1, rows + 1):
            subsidiary_data = {}
            index = 1
            for column in range(1, columns + 1):
                path = f"//*[@id = 'subsidiaryTable']/tbody/tr[{row}]/td[{column}]"
                try:
                    data = driver.find_element_by_xpath(path).text
                    subsidiary_data[dic[index]] = data
                    index += 1
                except:
                    subsidiary_data[dic[index]] = None
                    index += 1
            time.sleep(5)
            subsidiaries.append(subsidiary_data)

    time.sleep(10)
    return {"Subsidiary": subsidiaries}
