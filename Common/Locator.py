from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver

class Locator:

    driver = webdriver.Chrome()
    def GetPage(self,url):
        self.driver.get(url);
    #get Page
    #driver.get("xxxxxx")

    #Get Elements
    def GetElement_ByClassName(self,str):
        element = self.driver.find_elements(By.CLASS_NAME, str)
        return element

    def GetElement_ById(self,str):
        element = self.driver.find_element(by=By.ID, value=str)
        return element

    def GetElement_ByTag(self,str):
        element = self.driver.find_element(By.TAG_NAME, str)
        return element

    def GetElement_ByName(self,name):
        element = self.driver.find_element(By.NAME, name)
        return element

    def GetElement_ByLinkText(self,txt):
        element = self.driver.find_element(By.LINK_TEXT, txt)
        return element

    def GetElement_ByCSS(self,txt):
        #driver.find_element(By.CSS_SELECTOR, "#food span.dairy.aged")
        element = self.driver.find_element(By.CSS_SELECTOR, txt)
        return element

    def GetElement_ByPartialLinkText(self,txt):
        element = self.driver.find_element(By.PARTIAL_LINK_TEXT, txt)
        return element

    def GetElement_ByXpath(self,pathurl):
        element = self.driver.find_elements(By.XPATH, pathurl)
        return element

    def Fill_ByClassname(self,classname):
        element = self.GetElement_ByClassName(classname)
        element.send_keys(classname)

    def Fill_ById(self):






