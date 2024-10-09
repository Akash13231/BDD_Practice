

from behave import *
from handler import Handler_file
from shopping import ShoppingItem

log = Handler_file.getLogger()

@given('page url is given "{url}"')
def step_url(context, url):
    status = False
    try:
        shop = ShoppingItem(context.driver)
        shop.open_page(url)
        title = context.driver.title
        assert 'ProtoCommerce' in title, 'title is wrong'
        log.info(f'{url} page opened')
        status = True
    except Exception as e:
        log.error(f'Error occurred : {e}')
    assert  status is True


@when('Item want to purchase')
def step_item_select(context):
    status = False
    try:
        shop = ShoppingItem(context.driver)
        shop.shopitem().click()
        shop.product_selection().click()
        shop.checkout().click()
        shop.purchase_page().click()
        log.info('purchase button clicked')
        status = True
    except Exception as e:
        log.error(f'Exception occured {e}')
    assert status is True


@Then('sucess message appears for second')
def step_success(context):
    status = False
    try:
        shop = ShoppingItem(context.driver)
        alert_text = shop.success_msg().text
        log.info(alert_text)
        assert ('Success' in alert_text)
        status = True

    except Exception as e:
        log.error(f'exception occured: {e}')
    assert status is True, 'Error message is wrong'



