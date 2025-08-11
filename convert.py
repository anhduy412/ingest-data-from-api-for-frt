# convert with no function or def 
# This script is intended to be run as a standalone script.
import pandas as pd

data = pd.read_excel("Book1.xlsx", sheet_name="Sheet1")
data = data.to_csv("disease.csv", index=False, encoding="utf-8-sig")
print("Conversion completed successfully. The data has been saved to 'disease.csv'.")