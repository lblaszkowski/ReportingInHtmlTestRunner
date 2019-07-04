import unittest
from selenium import webdriver
from time import sleep
import HtmlTestRunner


url = 'https://www.tineye.com/'

class UploadImagePage(unittest.TestCase):

    @classmethod
    def setUp(self, browser="mozilla"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_75/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        elif browser == "mozilla":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url)
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_UploadImagePage(self):
        driver = self.driver
        button_image = driver.find_element_by_id("upload-button")
        button_image.click()
        upload_image = driver.find_element_by_id("upload_box")
        upload_image.send_keys('C:\\ReportingInHtmlTestRunner\\PageObjectModel\\image\\surfer-2335088_960_720.jpg')
        sleep(5)

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/ReportingInHtmlTestRunner/PageObjectModel/Reports'))



