from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import logging


class BaseView:
    def __init__(self,driver):
        '''

        :param driver: 初始化driver
        '''
        self.driver = driver


    def find_element(self,*loc):
        '''
        查找单个元素
        :param loc:
        :return:
        '''
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(loc))
        WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable(loc))
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)


    def find_elements(self,*loc):
        '''
        查找一组元素
        :param loc:
        :return:
        '''
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located(loc))
        WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable(loc))
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located(loc))
        return self.driver.find_elements(*loc)

    def inputValue(self, inputBox, value):
        """
        在输入框写值
        :param inputBox:
        :param value:
        :return:
        """
        inputB = self.find_element(*inputBox)

        # inputB.clear()
        inputB.send_keys(value)

    def clickbutton(self, inputBox):
        """
        点击按钮
        :param inputBox:
        :param value:
        :return:
        """
        buttonclick = self.find_element(*inputBox)
        buttonclick.click()

    def getValue(self, *loc):
        """
        返回元素的text文本值
        :param loc:
        :return:
        """
        element = self.find_element(*loc)
        value = element.text
        return value

    def save_image(self,filename):
        logging.info('Fail Screenshot')
        func_path = os.path.dirname(os.path.dirname(__file__))
        file_path = str(func_path)+"/image/"+filename
        self.driver.get_screenshot_as_file(file_path)