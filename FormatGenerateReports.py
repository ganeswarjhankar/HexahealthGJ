import pandas as pd

class ReportGenerator:
    def __init__(self, filename):
        self.data = pd.read_excel(filename)

    def generate_report(self, filename):
        # Write the DataFrame to an Excel file
        self.data.to_excel(filename, index=False)

# Instantiate the class and pass in the file name
generator = ReportGenerator("C:\\Users\\91928\\PycharmProjects\\GenerateReport - Copy.xlsx")

# Generate the report and save it to a fil
generator.generate_report("C:\\Users\\91928\\PycharmProjects\\GenerateReport.xlsx")

