from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver


    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    passw = (By.ID, 'exampleInputPassword1')
    checkbox = (By.ID, 'exampleCheck1')
    gender = (By.ID,'exampleFormControlSelect1')
    submit_button = (By.XPATH, "//input[@value='Submit']")
    dob = (By.NAME, 'bday')
    succ = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def open_page(self,url):
        return self.driver.get(url)

    def fill_name(self):
        return self.driver.find_element(*HomePage.name)

    def fill_elail(self):
        return self.driver.find_element(*HomePage.email)

    def fill_pass(self):
        return self.driver.find_element(*HomePage.passw)

    def check(self):
        return self.driver.find_element(*HomePage.checkbox)

    def fill_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def birth_date(self):
        return self.driver.find_element(*HomePage.dob)

    def submit(self):
        return self.driver.find_element(*HomePage.submit_button)

    def sucess(self):
        return self.driver.find_element(*HomePage.succ)

