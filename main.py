import time

import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

import methods
import xpaths
from xpaths import *
from nominationNames import *
from methods import *

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

URL = "https://www.cosmopolitan.in/cosmopolitan-india-blogger-awards-2024-nomination"

driver.get(URL)

time.sleep(10)

# Initialize an empty dictionary
award_dict = {}

for i in range(1, 23):
    xpath = "//li[@id='list_" + (str(i)) + "']/div/h2/label"
    award_name = driver.find_element(By.XPATH, xpath).text
    award_dict[award_name] = i

    open_file_and_insert('nomination_names.txt', award_name)

# print(award_dict)
desired_key = user_input(award_dict)
time.sleep(2)

name_of_influencer = input("Enter the name of the influencer: ")
ig_of_influencer = input("Enter the Instagram username of the influencer: ")

nomination_name_to_be_used = desired_key

textArea_to_write = "//h2/label[text()='" + nomination_name_to_be_used + "']/../following-sibling::textarea"
name_ig = name_of_influencer + "@" + ig_of_influencer

driver.find_element(By.XPATH, textArea_to_write).clear()
driver.find_element(By.XPATH, textArea_to_write).send_keys(name_ig)

file_to_login = open('data_1.txt', 'r+')

# reading each line from file
for line in file_to_login.readlines():
    global country_city, phone, mail, name

    # data is split into various sub-string separated with comma
    data = line.split(',')

    # signup till lines is not ending in file
    for i in range(0, len(data)):
        # print(data[i])

        name = data[0]
        mail = data[1]
        phone = data[2]
        country_city = data[3]
    print("----------------------------------------")
    print('\nCurrent name being used - ' + name)

    time.sleep(2)
    driver.refresh()
    driver.find_element(By.XPATH, xpaths.xpath_name).clear()
    driver.find_element(By.XPATH, xpaths.xpath_name).send_keys(name)
    driver.find_element(By.XPATH, xpaths.xpath_phone).clear()
    driver.find_element(By.XPATH, xpaths.xpath_phone).send_keys(phone)
    driver.find_element(By.XPATH, xpaths.xpath_email).clear()
    driver.find_element(By.XPATH, xpaths.xpath_email).send_keys(mail)
    driver.find_element(By.XPATH, xpaths.xpath_city).clear()
    driver.find_element(By.XPATH, xpaths.xpath_city).send_keys(country_city)

    driver.find_element(By.XPATH, xpath_termsConditons).click()

    driver.find_element(By.XPATH, xpath_submitBtn).click()

time.sleep(10)
driver.close()
