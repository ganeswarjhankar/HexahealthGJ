import FormatRandomUrlExcelMarketingCost
import FormatRandomUrlExcelMarketingDoctor
#import FormatGenerateReports
import marketingwhatsAppCheck
try:
    testcase1 = FormatRandomUrlExcelMarketingDoctor.MarketingDoctorPage()
    print("Marketing Doctor pages are passed")

except:
    print("Marketing Doctor pages are failed")

try:
    testcase2 = FormatRandomUrlExcelMarketingCost.MarketingPage()
    print("Marketing Cost Pages are passed")

except:
    print("Cost variant pages  are failed")

try:
    testcase3 = marketingwhatsAppCheck.MarketingPage()
    print("Marketing Whatsapp Pages are  Passed ")
except:
    print ("Marketing Whatsapp Pages are  Failed")