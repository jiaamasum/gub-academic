import pandas as pd

file_for_mv = pd.read_csv("CLP-02/missing_value.csv")
file_for_mv.columns = file_for_mv.columns.str.strip()  

file_for_mv['Revenue'] = pd.to_numeric(file_for_mv['Revenue'], errors='coerce')

file_filled = file_for_mv.fillna(file_for_mv.mean(numeric_only=True))

print(file_filled)