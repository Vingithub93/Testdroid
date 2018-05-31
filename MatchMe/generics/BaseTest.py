
import os
from appium import webdriver
from altunityrunner import AltrunUnityDriver
import subprocess
import pytest
from time import sleep


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
class BaseTest():

    altdriver = None
    driver=None
    eledriver=  None
    text= None
    platform = "android" # set to iOS to change platform
    
    @classmethod
    def setup_class(self):
        self.desired_caps = {}
        if (self.platform == "android"):
            self.desired_caps['platformName'] = 'Android'
            self.desired_caps['deviceName'] = 'device'
            self.desired_caps['app'] = PATH('../match.apk')
            self.desired_caps['newCommandTimeout'] = 400
            
        else: 
            self.desired_caps['platformName'] = 'iOS'
            self.desired_caps['deviceName'] = 'iPhone8'
            self.desired_caps['automationName'] = 'XCUITest'
            self.desired_caps['app'] = PATH('../../../match.ipa')

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.altdriver = AltrunUnityDriver(self.driver, self.platform)


    @classmethod
    def teardown_class(self):
        self.altdriver.stop()
        self.driver.quit()
      
if __name__ == '__main__':
    pytest.main()
