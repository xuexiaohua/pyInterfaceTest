import unittest
# import HTMLTestRunner
import logging
import pathMethod
import os
from common import genHtmlReport

logger=logging.getLogger()

class runAll:
    caseListFile = os.path.join(pathMethod.proDir, "caselist.txt")
    caseList=[]
    def set_case_list(self):
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_model = []

        for case in self.caseList:
            case_file = os.path.join(pathMethod.proDir, "testCase\\module\\exerciseTest")
            print(case_file)
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(case_file,
                                                           pattern=case_name + '.py',
                                                           top_level_dir=None)
            suite_model.append(discover)
            print("suite_model.length:")
            print(len(suite_model))

        if len(suite_model) > 0:
            print("===len(suite_model) > 0===")
            for suite in suite_model:
                for test_name in suite:
                    test_suite.addTest(test_name)
                    print("test_suit")
        else:
            return None
        return test_suite

    def run(self):
        try:
            print("run-self.set_case_suite()")
            suit = self.set_case_suite()
            print("run-self.set_case_suite().after")
            if suit is not None:
                print("suit is not None")
                logger.info("********TEST START********")
                print("logger.info")
                # fp = open(resultPath, 'wb')
                # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                # runner.run(suit)
                genHtmlReport(suit=suit,
                              title="Test Report",
                              description="Test Description",
                              verbosity=2,
                              casefile="casefile")
                print("genHtmlReport")
            else:
                logger.info("Have no case to test.")
                print("else")
        except Exception as ex:
            print("except")
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            # send test report by email
            # 调试
            # on_off="0"
            # if int(on_off) == 0:
            #     self.email.send_email()
            # elif int(on_off) == 1:
            #     logger.info("Doesn't send report email to developer.")
            # else:
            #     logger.info("Unknow state.")

if __name__=="__main__":
   runAll().run()