import os
from common.genTime import genCurrentTime

proDir=os.path.split(os.path.realpath(__file__))[0]
def getPath():
    return proDir

def isExistPath():
    dirName=genCurrentTime("%Y%m%d")
    result_report_path=proDir+"\\report\\"+dirName
    if not os.path.exists(result_report_path):
        os.makedirs(result_report_path)
    return result_report_path
