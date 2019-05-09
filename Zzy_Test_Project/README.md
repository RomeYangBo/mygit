#自动化测试环境的搭建过程
##安装Node.js 
[**Node.js**](https://nodejs.org/en/download/releases/)

- node.js版本为v11.3.0
- npm版本为v6.4.1
##安装Appium
###镜像设置
npm install -g cnpm --registry=https://registry.npm.taobao.org
###appium安装
cnpm install -g appium

- appium版本为v1.8.1
###安装appium-desktop
[**appium-desktop**](https://github.com/appium/appium-desktop/releases/)

- 用于元素定位
##python安装及配置
[**python**](https://www.python.org/getit/)

- python版本为v3.7.1

###安装Appium-Python-Client
pip install Appium-Python-Client
##JDK安装配置
[**JDK**](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html/)

- 配置环境变量
##Andriod sdk安装
[**Andriod sdk**](http://tools.android-studio.org/index.php/sdk/)

- 配置环境变量

##安装selenium
pip install selenium

#执行代码
## 目录结构

    ├── app		             //apk
    ├── baseView             //初始化driver，封装元素操作方法
    ├── common               //Appium会话配置及前置后置处理 
    ├── config               //日志配置
    ├── data                 //数据信息
    ├── image                //图片
    ├── logs                 //日志输出
	├──	reports				 //报告
	├──	test_case			 //测试用例
	└──	test_run			 //启动文件
###运行runTc.py文件
- 执行runner.run(descover)方法，加载测试用例,并执行login_Tc.py文件，并把执行结果写入报告文件
- 执行StartEnd类方法setUp，调用appium_desired方法安装并启动APP
- 创建driver对象，并调用expected_conditions方法进入登录首页
- 调用封装的输入与点击方法，数据与元素信息分别来源于data_info.py与longin_page.py
- 调用内容assert方法验证登录是否成功，如果失败则调用封装的截图方法保存失败时截图