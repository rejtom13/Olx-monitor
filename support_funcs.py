import json

import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

def PagingDiscordServer(webhook_url, text_message):
    return requests.post(webhook_url, data=json.dumps({ "content": text_message }), headers={ 'Content-Type': 'application/json',})


def wait_for_visibility_of_element(driver_instance, xpath, time_to_wait=20):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem

def is_visibility_of_element(driver_instance, xpath, time_to_wait=20):
    try:
        elem = WebDriverWait(driver_instance, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        elem = True
    except TimeoutException:
        elem = False
    return elem



def wait_for_invisibility_of_element(inv_driver_instance, xpath, time_to_wait=8):
    inv_elem = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_elem


def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()

