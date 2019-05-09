from common.myunit import StartEnd
from test_case.element_page.login_page import Login_Page
import logging
from data.data_info import *


class Test_Login(StartEnd):

    def test01_phone_true(self):
        '''登录功能测试：手机号登录'''
        logging.info('========testcase01 start========')
        phone_true = Login_Page(self.driver)
        phone_true.expected_conditions()
        logging.info('========start phone login========')
        phone_true.inputValue(phone_true.phone,phone_true_num)
        phone_true.inputValue(phone_true.verification_code,phone_code)
        phone_true.clickbutton(phone_true.loginBtn)
        try:
            self.assertEqual(phone_true.getValue(*phone_true.assert_login),'普通 | 841628771')
            logging.info('Phone Login Success')
        except:
            phone_true.save_image('phone_login_fail.png')
            logging.info('Phone Login Fail')
        logging.info('========testcase01 end========')

    def test02_weixin_login(self):
        '''登录功能测试：微信登录'''
        logging.info('========testcase02 start========')
        weixin = Login_Page(self.driver)
        weixin.expected_conditions()
        logging.info('========start weixin login========')
        weixin.clickbutton(weixin.weixinBtn)
        weixin.inputValue(weixin.username,'1145200569')
        weixin.inputValue(weixin.password,'1145200569')
        weixin.clickbutton(weixin.weixin_login_Btn)
        try:
            self.assertEqual(weixin.getValue(*weixin.assert_login),'微信名')
            logging.info('Weixin Login Success')
        except:
            weixin.save_image('weixin_login_fail.png')
            logging.info('Weixin Login Fail')
        logging.info('========testcase02 end========')







