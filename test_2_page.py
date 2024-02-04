from baseapp import BasePage
from time import sleep
from selenium.webdriver.common.by import By

CONTACT_LOCATOR = (By.LINK_TEXT,'Контакты')
REGION_LOCATOR = (By.CSS_SELECTOR,'.sbis_ru-Region-Chooser__text.sbis_ru-link')
PARTNERS_LOCATOR = (By.CSS_SELECTOR,'.controls-ListViewV.controls_list_theme-sbisru.controls-ListView_default.controls-itemActionsV_menu-hidden')
REGION_POPUP_LOCATOR = (By.CSS_SELECTOR,'.sbis_ru-Region-Panel__item')

class Test_2(BasePage):
    __test__ = False 

    def go_to_the_site(self, url):
        self.get(url)
    
    def click_on_the_contact_link(self):
        self.click(CONTACT_LOCATOR)
    
    def check_region(self, region):
        if self.find_element(REGION_LOCATOR).text == region:
        #self.get_element_text(REGION_LOCATOR) == region: 
            return True
        return False
    
    def get_partners_data(self):
        return self.find_element(PARTNERS_LOCATOR).text , self.driver.current_url, self.driver.title
    #self.get_element_text(PARTNERS_LOCATOR)

    def change_region(self,n):
        self.click(REGION_LOCATOR)
        self.find_elements(REGION_POPUP_LOCATOR)[n].click() #42
        sleep(1)
    