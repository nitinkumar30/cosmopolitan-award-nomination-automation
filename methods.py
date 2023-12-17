# from main import *
from selenium.webdriver.chrome import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver

import xpaths
# from main import driver


def webdriver_initialize():
    opt = webdriver.ChromeOptions()
    opt.add_argument("--start-maximized")
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=opt)
    # driver


def open_file_and_insert(filename, text):
    with open(filename, 'a') as file:
        # Write text to the file
        file.write(text)
        file.write("\n")


def import_from_file(file_path):
    global country_city, phone, mail, name

    file_to_login = open(file_path, 'r+')

    # reading each line from file
    for line in file_to_login.readlines():

        # data is split into various sub-string separated with comma
        data = line.split(',')

        # signup till lines is not ending in file
        for i in range(0, len(data)):
            # print(data[i])

            name = data[0]
            mail = data[1]
            phone = data[2]
            country_city = data[3]
            # profile = data[4]
            # rsnToBeSelected = data[5]
            print("----------------------------------------")
            print('\nCurrent name being used - '+name)


            # ---------------------------------------------

            # time.sleep(2)
            # driver.refresh()
            # driver.find_element(By.XPATH, xpaths.xpath_name).clear()
            # driver.find_element(By.XPATH, xpaths.xpath_name).send_keys(name)
            # driver.find_element(By.XPATH, xpaths.xpath_phone).clear()
            # driver.find_element(By.XPATH, xpaths.xpath_phone).send_keys(phone)
            # driver.find_element(By.XPATH, xpaths.xpath_email).clear()
            # driver.find_element(By.XPATH, xpaths.xpath_email).send_keys(mail)
            # driver.find_element(By.XPATH, xpaths.xpath_city).clear()
            # driver.find_element(By.XPATH, xpaths.xpath_city).send_keys(country_city)
            #
            # # send_keys_(xpaths.xpath_name, name)
            # # send_keys_(xpaths.xpath_phone, phone)
            # # send_keys_(xpaths.xpath_email, mail)
            # # send_keys_(xpaths.xpath_city, country_city)
            #
            # # click_element(xpaths.xpath_termsConditons)
            # driver.find_element(By.XPATH, xpath_termsConditons).click()
            #
            # # click_element(xpaths.xpath_submitBtn)
            # driver.find_element(By.XPATH, xpath_submitBtn).click()
    return name, mail, phone, country_city


def chromeOptions():
    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--disable-notifications')
    chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    desired_cap = chrome_options.to_capabilities()
    if desired_cap:
        print("Notifications blocked now !!!")


def user_input(award_dict):
    # Asking from user
    userInput_str = ""
    desired_key = None
    print("Enter the nomination no:\n")
    for name, index in award_dict.items():
        userInput_str += str(index) + ". " + name + "\n"

    user_input_ = int(input(userInput_str))
    for key, value in award_dict.items():
        if value == user_input_:
            desired_key = key
            print(f"The selected value for the input {user_input_} is: {desired_key}\n\n")
    return desired_key


# def send_keys_(xpath, text):
#     driver.find_element(By.XPATH, xpath).clear()
#     driver.find_element(By.XPATH, xpath).send_keys(text)
#
#
# def click_element(xpath):
#     driver.find_element(By.XPATH, xpath).click()
#
#
# def login_popup(xpath):
#     login_popup_ = driver.find_element(xpath)
#     if driver.find_element(xpath).is_displayed():
#         driver.find_element(xpath).click()
#         print("No need to login now.!!!")

