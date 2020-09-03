from selenium import webdriver
import time

class instagramBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()        

    def findPerson(self, handle):
        self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(handle)
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="/{}/"]'.format(handle)).click()
        time.sleep(2)

    def findPersonToDM(self, handle):
        self.driver.find_element_by_xpath("//input[@placeholder=\"Search\"]").send_keys(handle)
        time.sleep(1)
        self.driver.find_element_by_xpath('//a[@href="/{}/"]'.format(handle)).click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Message')]").click()

    def DM(self, message):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Message...']").send_keys(message)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Send')]").click()
    
    def Like(self):
        self.driver.find_element_by_xpath('//*[local-name()="svg" and @aria-label="Like"]/parent::span/parent::div/parent::button').click()
        
    def Comment(self, message):
        self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(message)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Post')]").click()

