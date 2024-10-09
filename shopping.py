from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from handler import Handler_file




class ShoppingItem():

    def __init__(self, driver):
        self.driver = driver


    def open_page(self,url):
        return self.driver.get(url)

    obj= (By.XPATH, "//a[text()='Shop']")
    def shopitem(self):
       return self.driver.find_element(*ShoppingItem.obj)





    checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    products_obj = (By.CLASS_NAME, 'card h-100')
    product_name = (By.XPATH, "div/h4/a")
    product_obj = (By.XPATH, 'div/button')

    def product_selection(self):
        products = self.driver.find_elements(*ShoppingItem.products_obj)

        for product in products:
            product_name = product.find_element(*ShoppingItem.product_name).text
            if product_name == 'Blackberry':
                product.find_element(*ShoppingItem.product_obj).click()
                break
        return  self.driver.find_element(*ShoppingItem.checkout_button)






    check_obj2 = (By.XPATH, "//button[@class='btn btn-success']")

    def checkout(self):
       return self.driver.find_element(*ShoppingItem.check_obj2)







    purchase_obj = ((By.ID, 'country'), (By.LINK_TEXT, 'India'), (By.XPATH, "//div[@class='checkbox checkbox-primary']"), (By.XPATH, "//input[@type='submit']"))


    def purchase_page(self):
        self.driver.find_element(*ShoppingItem.purchase_obj[0]).send_keys('ind')
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, 'India')))
        self.driver.find_element(*ShoppingItem.purchase_obj[1]).click()
        self.driver.find_element(*ShoppingItem.purchase_obj[2]).click()
        return self.driver.find_element(*ShoppingItem.purchase_obj[3])


    success_obj =(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
    def success_msg(self):
        return self.driver.find_element(*ShoppingItem.success_obj)


