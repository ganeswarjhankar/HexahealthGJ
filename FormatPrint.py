import pandas as pd

# Collect print statements into a list
output = []
for i in range(10):
    print_statement = "Print Statement {}".format(i)
    output.append(print_statement)
    print(print_statement)

# Convert the list to a pandas dataframe
df = pd.DataFrame(output, columns=["Output"])

# Write the dataframe to an Excel sheet
df.to_excel("C:\\Users\\91928\\PycharmProjects\\GenerateReport.xlsx", index=False)


class PrintExcel:
    pass