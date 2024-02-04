from selenium.common.exceptions import StaleElementReferenceException

n_trials = 3

class BasePage:

    def __init__(self, driver) :
        self.driver=driver
    
    def get(self,url):
        self.driver.get(url)
    
    def click(self, locator):
        for i in range(n_trials):
            try:
                self.driver.find_element(*locator).click()
            except StaleElementReferenceException:
                continue
            else:
                break

    def find_element(self,locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def switch_window(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])