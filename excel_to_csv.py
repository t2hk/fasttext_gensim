import pandas as pd
import glob, sys

args = sys.argv
excel_dir = args[1]

files = glob.glob(excel_dir + '/*.xls*')

for file in files:
  excel = pd.ExcelFile(file, encoding='utf8')

  sheet_names = excel.sheet_names
  for i, name in enumerate(sheet_names):
    csv_file = file.replace(".xlsx", "").replace(".xls", "") + '_' + str(i) + '.csv'
    sheet_df = excel.parse(name, header=[0, 1])
    #sheet_df.to_csv(csv_file)
    columns_val = sheet_df.columns.values

    col_names = []
    for col_vals in columns_val:
        col_name = col_vals[0].replace('\n', '') + '_' + col_vals[1].replace('\n','')
        if 'Unnamed' in col_vals[1]:
            col_name = col_vals[0].replace('\n','')
        col_names.append(col_name)
    sheet_df.columns = col_names

    sheet_df.to_csv(csv_file)
