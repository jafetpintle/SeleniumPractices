import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class HelloWorld(unittest.TestCase):
   
    def setUp(self):
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        self.driver.get('http://demo-store.seleniumacademy.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID, 'search')

    def test_search_field_by_name(self) -> None:
        search_field = self.driver.find_element(By.NAME, 'q')
    
    def test_search_field_by_class(self) -> None:
        search_field = self.driver.find_element(By.CLASS_NAME, 'input-text')
    
    def test_search_button_enabled(self) -> None:
        button = self.driver.find_element(By.CLASS_NAME, 'button')
    
    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element(By.CLASS_NAME, 'promos')
        banners = banner_list.find_elements(By.TAG_NAME, 'img')
        self.assertEqual(3, len(banners))
    def test_vip_promo(self) -> None:
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[3]/a/img')
    def test_shopping_car(self)->None:
        shopping_car_icon = self.driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)