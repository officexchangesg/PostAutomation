from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from enum import Enum


class SeedOptions(Enum):
        ClassName = 0
        Id = 1
        Tag = 2
        Name = 3
        CSS = 4
        LinkText = 5
        PartialLinkTxt = 6
        XPath = 7

LocatorSeedOptions = {
    SeedOptions.ClassName : By.CLASS_NAME,
    SeedOptions.Id : By.ID      ,
    SeedOptions.Tag : By.TAG_NAME,
    SeedOptions.Name : By.NAME,
    SeedOptions.CSS : By.CSS_SELECTOR,
    SeedOptions.LinkText : By.LINK_TEXT,
    SeedOptions.PartialLinkTxt : By.PARTIAL_LINK_TEXT,
    SeedOptions.XPath : By.XPATH
}

class Locator:

    driver = webdriver.Chrome()
    def GetPage(self,url):
        self.driver.get(url)
    #get Page
    #driver.get("xxxxxx")

    #Get Elements
    def GetElement(self,SeedOptions,str):
        element = self.driver.find_elements(LocatorSeedOptions.get(SeedOptions), str)
        return element

    def Fill_Element(self,SeedOptions,str):
        self.GetElement(SeedOptions,str).send_keys("Testing")

 





