import time
from logging import setLogRecordFactory

import pytest
from behave import *
from behave.reporter.summary import status_order
from selenium.webdriver.support.select import Select
from logs import log_file
from HomePage import HomePage

log = log_file.getLogger()

@when('all date for form fill given "{firstname}", "{email}", "{gender}", "{dob}", "{passw}"')
def step_impl(context,firstname, email, gender,dob, passw):
    status = False
    try:
        homepage = HomePage(context.driver)
        homepage.open_page()
        log.info('page opened')
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
