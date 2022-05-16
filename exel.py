import pandas as pd


sheets = [
    "Group A",
    "Group B",
    "Group C",
    "Group D"
]


ex_data = pd.read_excel(r'C:\Users\Togrul\Desktop\This one\Analysis_Grade sheet L0 for sts.xlsx', sheet_name = sheets)

print(type(ex_data["Group A"]))



