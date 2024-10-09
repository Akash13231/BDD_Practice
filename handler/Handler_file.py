import inspect
import logging
import os
from datetime import datetime, date
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class AllureLoggingHandler(logging.Handler):
    def log(self,level_name, message):
        with allure.step(f"Log {level_name} {message}"):
            if level_name.lower() == 'error':
                attach_screenshoot()

    def emit(self, record):
        self.log(record.levelname, record.getMessage())


def getLogger():
    allure_handler = AllureLoggingHandler()
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    filehandler = logging.FileHandler \
        ('C:/Users/abhosage/PycharmProjects/Testing/BDD_testing/logfile.log')
    formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formater)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(allure_handler)
    return logger


def attach_screenshoot():
    driver = logging.FileHandler.selenium_driver
    current_date_time = str(f'({(date.today().strftime("%d %b"))} {(datetime.now().strftime("%H_%M_%S"))})')
    screenshot_path = os.path.join(os.path.abspath(__file__ + '/../../'), f"failed_screenshots/{current_date_time}.png")
    driver.get_screenshot_as_file(screenshot_path)
    allure.attach.file(source=screenshot_path, attachment_type=allure.attachment_type.PNG, name='screenshot')

def waitmechanism(self, text):
    wait = WebDriverWait(self.driver, 10)
    wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, text)))
