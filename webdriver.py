from itertools import dropwhile

from selenium import webdriver

def get_webdriver(webdriver_type):
    if webdriver_type == 'edge':
        driver = webdriver.Edge()
    elif webdriver_type == 'firefox':
        driver= webdriver.Firefox()
    else:
        driver= webdriver.Chrome()
    return driver
