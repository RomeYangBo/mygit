from baseView.baseView import BaseView
from selenium.webdriver.common.by import By
import time
import logging

class Login_Page(BaseView):



    def expected_conditions(self):
        logging.info('========Go to my homepage========')
        time.sleep(5)
        try:
            self.clickbutton(self.myBtn)
            self.clickbutton(self.head_picture)
        except:
            time.sleep(3)
            self.clickbutton(self.myBtn)
            self.clickbutton(self.head_picture)

    #========================页面元素=========================
    #我的
    myBtn = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[3]')
    #头像
    head_picture = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]/android.view.View[1]/android.widget.ImageView[1]')
    #手机号
    phone = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[1]')
    #验证码
    verification_code = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    #登录按钮
    loginBtn = (By.CLASS_NAME,'android.widget.Button')
    #验证登录
    assert_login = (By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[1]/android.view.View[1]')

    #===========================微信登录=======================
    #微信按钮
    weixinBtn = (By.XPATH,'	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.ImageView')
    #微信账号密码列表
    username = (By.XPATH,'//android.widget.FrameLayout[@content-desc="当前所在页面,登录微信"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.EditText')
    password = (By.XPATH,'//android.widget.FrameLayout[@content-desc="当前所在页面,登录微信"]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText')
    #微信登录按钮
    weixin_login_Btn = (By.ID,'com.tencent.mm:id/cqc')