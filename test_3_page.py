import re
from baseapp import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from os import getcwd, stat, remove
from os.path import exists

COOKIE_LOCATOR = (By.XPATH,'/html/body/div[1]/div/div/div[2]/div[1]/div[3]/div[2]/div[2]')
DOWNLOAD_PAGE_LOCATOR = (By.XPATH,'//*[@id="container"]/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a')
PLUGIN_LOCATOR = (By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[2]/div[2]')
DOWNLOAD_LINK_LOCATOR = (By.XPATH,'/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')


class Test_3(BasePage):
    __test__ = False 
    
    def go_to_the_site(self, url):
        self.driver.get(url)
    
    def click_on_the_cookie(self):
        self.click(COOKIE_LOCATOR)
    
    def click_on_download_page(self):
        self.click(DOWNLOAD_PAGE_LOCATOR)
        sleep(2)
    
    def click_plugin_page(self):
        self.click(PLUGIN_LOCATOR)
        sleep(2)
    
    def click_download(self):
        self.click(DOWNLOAD_LINK_LOCATOR)
        self.file_path = getcwd()+'/'+self.driver.find_element(*DOWNLOAD_LINK_LOCATOR).get_attribute('href').split('/')[-1]
        sleep(0.5)
    
    def wait_download(self):
        while exists(self.file_path+'.crdownload'): #getcwd()+'/sbisplugin-setup-web.exe.crdownload'
            sleep(0.5)

    def check_size(self):
        file_stats = stat(self.file_path)
        remove(self.file_path)
        expected_file_size = re.findall("\\d+\\.\\d+", self.driver.find_element(*DOWNLOAD_LINK_LOCATOR).text)[0]
        real_file_size = f'{file_stats.st_size / (1024 * 1024)}'
        if expected_file_size == real_file_size[:len(expected_file_size)]:
            return True
        return False
