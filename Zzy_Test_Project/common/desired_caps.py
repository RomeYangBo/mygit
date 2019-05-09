from appium import webdriver
import logging
import logging.config
import os


CON_LOG = '../config/log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()

base_path = os.path.dirname(os.path.dirname(__file__))
app_path = os.path.join(base_path,'app','zhangzhongyun-1.5.3-88650.apk')

def appium_desired():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = '127.0.0.1:21503'
    desired_caps['platforVersion'] = '5.1.1'
    desired_caps['app'] = app_path
    desired_caps['appPackage'] = 'com.zhangzhongyun.store'
    desired_caps['appActivity'] = 'com.zhangzhongyun.inovel.MainActivity'
    desired_caps['noReset'] = 'True'
    # desired_caps['automationName']='uiautomator2'

    logging.info('===========start APP==============')
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
    driver.implicitly_wait(8)
    return driver

if __name__ == '__main__':
    appium_desired()