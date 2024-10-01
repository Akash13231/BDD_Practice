

# This is definitions file for the .features files


import time
from logging import setLogRecordFactory
from os.path import isabs

import pytest
from behave import *
from behave.reporter.summary import status_order
from selenium.webdriver.support.expected_conditions import title_is
from selenium.webdriver.support.select import Select
from logs import log_file
from HomePage import HomePage

log = log_file.getLogger()

@given('url is given "{url}"')
def step_url(context, url):
    status = False
    try:
        homepage = HomePage(context.driver)
        homepage.open_page(url)
        title = context.driver.title
        assert 'ProtoCommerce' in title, 'title is wrong'
        log.info(f'{url} page opened')
        status = True
    except Exception as e:
        log.error(f'Error occured : {e}')
    assert  status is True

@when('all date for form fill entered "{firstname}", "{email}", "{gender}", "{dob}", "{passw}"')
def step_impl(context,firstname, email, gender,dob, passw):
    status = False
    try:
        homepage = HomePage(context.driver)
        homepage.fill_name().send_keys(firstname)
        homepage.fill_elail().send_keys(email)
        homepage.fill_pass().send_keys(passw)
        homepage.check().click()
        sel = Select(homepage.fill_gender())
        sel.select_by_visible_text(gender)
        time.sleep(2)
        homepage.birth_date().send_keys(dob)
        homepage.submit().click()
        log.info('submit button clicked')
        status = True
    except Exception as e:
        log.error(f"Exception Occured: {e}")
    assert status is True

@then("sucess message appears")
def steps_sucess(context):
    status = False
    try:
        homepage = HomePage(context.driver)
        alert_text = homepage.sucess().text
        log.info(alert_text)
        assert ('Success' in alert_text)
        context.driver.refresh()
        status = True
    except Exception as e:
        log.error(f'exception occured: {e}')
    assert status is True, 'Error message is wrong'
