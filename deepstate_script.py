from PIL import Image
import time
import io
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class DeepstateNavigator:
    def __init__(self, headless=True):
        self.headless = headless
        self.options = Options()
        if self.headless:
            self.options.add_argument("--headless")
        else:
            self.options.add_argument("--start-maximized")
        self.webdriver_service = Service('geckodriver')
        self.driver = webdriver.Firefox(service=self.webdriver_service, options=self.options)
        self.url = 'https://deepstatemap.live/'
        self.options = '#6/49.232/34.948'
        
    def click_by_classname(self, class_name):
        ActionChains(self.driver).click().perform()
        button_ = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        button_.click()
        time.sleep(1)
        
    def click_filter_and_toggle(self):
        self.click_by_classname('filter-icon')
        all_checkbox_label = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@title="Все"]')))
        all_checkbox_switch = all_checkbox_label.find_element(By.CLASS_NAME, 'toggle-switch')
        all_checkbox_switch.click()
        time.sleep(1)

    def extract_color_map(self):
        self.driver.get(self.url+self.options)
        time.sleep(2)
        self.click_by_classname('agree')
        self.click_filter_and_toggle()
        img   = self.get_screenshot()
        img   = self.get_cropped(img)
        if self.headless:
            img.show()
        self.save(img)
        self.quit()

    def get_screenshot(self):
        png = self.driver.get_screenshot_as_png()
        image = Image.open(io.BytesIO(png))
        return image

    def get_cropped(self, image, position=(101, 98), to_crop_size=(825, 550)):
        box = (position[0], position[1], position[0] + to_crop_size[0], position[1] + to_crop_size[1])
        cropped_img = image.crop(box)
        return cropped_img
    
    def save(self,img):
        now_ = time.time()
        img.save(f"images/screenshot_{now_}.png")
        
    def quit(self):
        self.driver.quit()


# Bucle principal para mantener el script en ejecución
while True:
    web_navigator = DeepstateNavigator()
    web_navigator.extract_color_map()
    time.sleep(12*3600)
