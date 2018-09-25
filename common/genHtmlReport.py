from common import getOsPath
from common import genTime
from HTMLTestRunner import HTMLTestRunner

def generateHtmlReport(suit,title,description,verbosity):
    relativePath= getOsPath.getPath()
    filename= open(relativePath
                   + '\\report'
                   + '\\testResult_report' + genTime.genCurrentTime("%Y%m%d%H%M%S") + '.html',"wb")
    runner = HTMLTestRunner(stream=filename,
                            verbosity=verbosity,
                            title=title,
                            description=description)
    runner.run(suit)