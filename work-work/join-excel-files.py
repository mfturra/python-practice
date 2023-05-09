# Import required modules
import glob2 # Finds all path names that match a specific pattern
import pandas as pd

# Specify paths to files
path = r'C:\Users\MT1070\Desktop\Master Call Volume'


# Display names of files in folder
file_names = glob2.glob(path + "/*.xlsx")


# Initialize an empty data frame to store data from all files
final_sheet = pd.DataFrame()


# Iteratively read data extracts and append them to one final df 
for file in file_names:
    # Combine excel sheets into single df
    df = pd.concat(pd.read_excel(file, sheet_name=None, skipfooter=2), ignore_index=True, sort=False) # without engine 
    # df = pd.concat(pd.read_excel(file, sheet_name=None, engine='openpyxl'), ignore_index=True, sort=False)

    # Append excel files one by one
    final_sheet = final_sheet.append(df, ignore_index=True)


# Combine data into a new Excel file
master_file_path = r"C:\Users\MT1070\Desktop\Master Call Volume\SpinSci Call Volume Evaluation.xlsx"
final_sheet.to_excel(master_file_path, sheet_name='Raw Data', index=False)