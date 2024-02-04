import pytest
from test_1_page import Test_1
from test_2_page import Test_2
from test_3_page import Test_3

def test_1(driver):
    test = Test_1(driver)
    test.go_to_site('https://sbis.ru/')
    test.click_on_the_contact_link()
    test.click_on_the_logo()
    test.click_on_the_cookie()
    assert test.check_power_in_people()== True , 'отсутствует блок сила в людях'
    test.click_about()
    assert test.check_current_url('https://tensor.ru/about') == True, 'не верный url'
    assert test.check_images_equality() == True , 'изображения имеют разный размер'

def test_2(driver):
    test = Test_2(driver)
    test.go_to_the_site('https://sbis.ru/')
    test.click_on_the_contact_link()
    assert test.check_region('Ярославская обл.') == True ,'не верно определен регион' #Ленинградская обл.   Ярославская обл. 
    last_partners, last_url, last_title = test.get_partners_data()
    test.change_region(42)
    assert test.check_region('Камчатский край') == True ,'не верно определен регион после смены региона'
    partners, url, title = test.get_partners_data() 
    assert last_partners != partners and last_url != url and last_title != title ,'контент идентичен после смены региона'

def test_3(driver):
    test = Test_3(driver)
    test.go_to_the_site('https://sbis.ru/')
    test.click_on_the_cookie()
    test.click_on_download_page()
    test.click_plugin_page()
    test.click_download()
    test.wait_download()
    assert test.check_size() == True, 'размеры файлов не равны'
