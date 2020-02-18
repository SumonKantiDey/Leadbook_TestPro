import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import date, datetime

options = Options()
options.add_argument("--headless")


def _setup():
    company_profile = "https://www.idx.co.id/en-us/listed-companies/company-profiles/"
    chrome_driver = "D:/Leadbook/crawled_data/driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    driver.get(company_profile)
    driver.find_element_by_xpath(
        "//*[@id='companyTable_length']/label/select/option[4]").click()
    return driver


dic = {
    1: "ticker symbol",
    2: "company name",
    3: "url",
    4: "listing_date",
    5: "crawled_at"
}


def _pagination_index(page):
    pagination = f"//*[@id='companyTable_paginate']/span/a[{page}]"
    return pagination


def _table_path(tr, td):
    table_index = f"//*[@id='companyTable']/tbody/tr[{tr}]/td[{td}]"
    return table_index


def _click_option():
    option = "//*[@id='companyTable_length']/label/select/option[4]"
    return option


def _get_row_columns(driver, page):
    rows = len(driver.find_elements_by_xpath(
        ".//*[@id='companyTable']/tbody/tr"))
    columns = len(driver.find_elements_by_xpath(
        f".//*[@id='companyTable']/tbody/tr[{page}]/td"))
    return rows, columns


def _store_data(company_data):
    if os.path.exists("company_index.json") == False:
        store_data = []
        store_data.append(company_data)
        with open('company_index.json', 'w') as fp:
            json.dump(store_data, fp)
    else:
        with open('company_index.json', 'r') as fp:
            data = json.load(fp)
        data.append(company_data)
        with open('company_index.json', 'w') as fp:
            json.dump(data, fp)
    return


def _data_parse(start_pg, end_pg):
    for page in range(start_pg, end_pg):
        driver = _setup()
        time.sleep(10)
        pagination = _pagination_index(page)
        driver.find_element_by_xpath(pagination).click()
        option = _click_option()
        driver.find_element_by_xpath(option).click()
        rows, columns = _get_row_columns(driver, page)
        for row in range(1, rows + 1):
            company_data = {}
            index = 1
            for col in range(1, columns+1):  # per row column
                path = _table_path(row, col)
                if col == 3:
                    url = path + '/a'
                    try:
                        company_name = driver.find_element_by_xpath(path).text
                        company_data[dic[index]] = company_name
                        index += 1
                    except:
                        company_data[dic[index]] = None
                        index += 1
                    try:
                        company_url = driver.find_element_by_xpath(
                            url).get_attribute("href")
                        company_data[dic[index]] = company_url
                        index += 1
                    except:
                        company_data[dic[index]] = None
                        index += 1
                else:
                    if col == 1:
                        txt = driver.find_element_by_xpath(path).text
                    else:
                        try:
                            company_info = driver.find_element_by_xpath(
                                path).text
                            company_data[dic[index]] = company_info
                            index += 1
                        except:
                            company_data[dic[index]] = None
                            index += 1
                company_data[dic[index]] = str(date.today())
                time.sleep(5)
            company_data['listing_date'] = str(datetime.strptime(
                company_data['listing_date'], '%d %b %Y').date())
            print(company_data)
            _store_data(company_data)
        time.sleep(10)


if __name__ == "__main__":
    driver = _setup()
    time.sleep(10)
    page_url = "//*[@id='companyTable_paginate']/span/a"
    pages = len(driver.find_elements_by_xpath(page_url))
    pages = pages + 1
    _data_parse(1, pages)
