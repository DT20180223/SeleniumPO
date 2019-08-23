import unittest
import HTMLTestRunner_cn
import os

file_path1 = os.path.join(os.getcwd(),"report",'11.html')
f = open(file_path1,'wb')
# file_name = "11.html"
# report_file = os.path.join()


if __name__=="__main__":
    testuint = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(r'F:\PycharmProjects\SeleniumPO\testcase',pattern='test*.py',top_level_dir=None)
    testuint.addTest(discover)
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=f,title="测试报告",description=u'用例执行情况:',verbosity=2)
    runner.run(testuint)


