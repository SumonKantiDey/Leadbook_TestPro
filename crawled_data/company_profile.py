import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from datetime import date, datetime
import json
from company_subsidiary import _subsidiary
options = Options()
options.add_argument("--headless")
store_data = []


def _setup():
    chrome_driver = "D:/Leadbook/crawled_data/driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    return driver


def _read_json_file():
    company_list = []
    company_name = []
    with open('company_index.json', 'r') as f:
        data = json.load(f)
    for profile in data:
        company_list.append(profile['url'])
        company_name.append(profile['ticker symbol'])
    return company_list, company_name


def _general_info(driver, company_profile):
    general_info = {}
    driver.get(company_profile)
    time.sleep(10)
    general_info_path = "//*[@id='general']/dl/dt"
    data_length = len(driver.find_elements_by_xpath(general_info_path))
    for length in range(1, data_length + 1):
        title_url = f"//*[@id='general']/dl/dt[{length}]"
        description_url = f"//*[@id='general']/dl/dd[{length}]"
        title = driver.find_elements_by_xpath(title_url)[0].text
        try:
            description = driver.find_elements_by_xpath(description_url)[
                0].text
            general_info[title] = description
        except:
            general_info[title] = None
    return general_info


def _corporate_secretary(driver, company_profile):
    dic = {
        1: "name",
        2: "email",
        3: "phone"
    }
    corporate_secretary = []
    driver.get(company_profile)
    time.sleep(10)
    secretary_info_path = "//*[@id='csTable']/tbody/tr"
    rows = len(driver.find_elements_by_xpath(secretary_info_path))
    columns_path = "//*[@id='csTable']/tbody/tr[1]/td"
    columns = len(driver.find_elements_by_xpath(columns_path))
    for row in range(1, rows + 1):
        secretary_dic = {}
        index = 1
        for column in range(1, columns + 1):
            path = f"//*[@id= 'csTable']/tbody/tr[{row}]/td[{column}]"
            try:
                secretary_dic[dic[index]] = driver.find_elements_by_xpath(path)[
                    0].text
                index += 1
            except:
                secretary_dic[dic[index]] = None
                index += 1
        corporate_secretary.append(secretary_dic)
    return {"Corporate Secretary": corporate_secretary}


def _director(driver, company_profile):
    dic = {
        1: "name",
        2: "Position"
    }
    director = []
    driver = _setup()
    driver.get(company_profile)
    time.sleep(10)
    director_info_path = "//*[@id = 'directorTable']/tbody/tr"
    rows = len(driver.find_elements_by_xpath(director_info_path))
    for row in range(1, rows + 1):
        director_dic = {}
        index = 1
        for column in range(1, 3):
            path = f"//*[@id= 'directorTable']/tbody/tr[{row}]/td[{column}]"
            try:
                director_dic[dic[index]] = driver.find_elements_by_xpath(path)[
                    0].text
                index += 1
            except:
                director_dic[dic[index]] = None
                index += 1
        director.append(director_dic)
        time.sleep(5)
    return {"Director": director}


def _store_data(company_data):
    if os.path.exists("company_profile.json") == False:
        store_data = []
        store_data.append(company_data)
        with open('company_profile.json', 'w') as fp:
            json.dump(store_data, fp)
    else:
        with open('company_profile.json', 'r') as fp:
            data = json.load(fp)
        data.append(company_data)
        with open('company_profile.json', 'w') as fp:
            json.dump(data, fp)
    return


if __name__ == "__main__":

    data, name = _read_json_file()

    for index in range(len(data)):
        company_profile = data[index]
        driver = _setup()
        general_info = _general_info(driver, company_profile)
        corporate_secretary = _corporate_secretary(driver, company_profile)
        director = _director(driver, company_profile)
        subsidiaries = _subsidiary(driver, company_profile)
        company_profile_info = {**general_info,
                                **corporate_secretary, **director, **subsidiaries}
        _store_data(company_profile_info)
        time.sleep(10)
