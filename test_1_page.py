from baseapp import BasePage
from selenium.webdriver.common.by import By

CONTACTS_LOCATOR = (By.LINK_TEXT,'Контакты')
LOGO_LOCATOR = (By.CSS_SELECTOR,'.sbisru-Contacts__logo-tensor.mb-12')
POWER_IN_PEOPLE_LOCATOR = (By.XPATH,'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
COCKIE_LOCATOR = (By.CSS_SELECTOR,'.tensor_ru-CookieAgreement__close')
ABOUT_CLICK_LOCATOR = (By.XPATH,'//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
IMGS_SELECTOR = (By.CSS_SELECTOR,'.s-Grid-container a img')

class Test_1(BasePage):
    __test__ = False  
    
    def go_to_site(self,url):
        self.get(url)
    
    def click_on_the_contact_link(self):
        self.click(CONTACTS_LOCATOR)
    
    def click_on_the_logo(self):
        self.click(LOGO_LOCATOR)
        self.switch_window(1)
    
    def click_on_the_cookie(self):
        self.click(COCKIE_LOCATOR)
    
    def check_power_in_people(self):
        try:
            self.find_element(POWER_IN_PEOPLE_LOCATOR)
            return True
        except:
            return False
    
    def click_about(self):
        self.click(ABOUT_CLICK_LOCATOR)
    
    def check_current_url(self, url):
        return self.driver.current_url == url
    
    def check_images_equality(self):
        imgs = self.find_elements(IMGS_SELECTOR)
        imgs = [(e.get_attribute('width'),e.get_attribute('height')) for e in imgs]
        for i in imgs:
            if i != imgs[0]:
                return False
        return True


    

