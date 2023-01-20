import FormatRandomUrlExcelMarketingCost
import FormatRandomUrlExcelMarketingDoctor
import FormatGenerateReports
try:
    testcase1 = FormatRandomUrlExcelMarketingDoctor.MarketingDoctorPage()
    report1 = FormatGenerateReports.ReportGenerator(1)

except:
    print("testcase1 failed")

try:
    testcase2 = FormatRandomUrlExcelMarketingCost.MarketingPage()

except:
    print("testcase2 failed")