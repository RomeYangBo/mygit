import unittest
from BSTestRunner import BSTestRunner
import time
import os


testcase_dir = '../test_case'
report_dir = os.path.dirname(os.path.dirname(__file__))

#加载测试用例
discover = unittest.defaultTestLoader.discover(testcase_dir,pattern='login_Tc.py')

now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir +'/reports/' + now + 'test_report.html'

with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='Zzy Test Report',description='Zzy Andriod App Test Report')
    runner.run(discover)