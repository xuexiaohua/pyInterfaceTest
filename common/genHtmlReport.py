import pathMethod
from common import genTime
from HTMLTestRunner import HTMLTestRunner

def generateHtmlReport(suit,title,description,verbosity,casefile):
    report_Path = pathMethod.isExistPath()
    filename= open(report_Path
                   + '\\'
                   + casefile
                   + genTime.genCurrentTime("%Y%m%d%H%M%S")
                   + '.html',"wb")
    runner = HTMLTestRunner(stream=filename,
                            verbosity=verbosity,
                            title=title,
                            description=description)
    runner.run(suit)