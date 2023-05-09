# Import required modules
import glob2 # Finds all path names that match a specific pattern
import pandas as pd

# Specify paths to files
path = r'C:\Users\MT1070\Desktop\Master Call Volume'


# Display names of files in folder
file_names = glob2.glob(path + "/*.xlsx")

## Print a list of all files located in folder in terminal
# print(f"\nFile names: {file_names}\n")

# Initialize an empty data frame to store data from all files
final_sheet = pd.DataFrame()

for file in file_names:
    # Combine excel sheets into single df
    df = pd.concat(pd.read_excel(file, sheet_name=None), ignore_index=True, sort=False) # without engine 
    # df = pd.concat(pd.read_excel(file, sheet_name=None, engine='openpyxl'), ignore_index=True, sort=False)

    # Append excel files one by one
    final_sheet = final_sheet.append(df, ignore_index=True)
    

# breakpoint("Stopped here")
# Print the combined data set
# print(f'\nFinal Sheet:{final_sheet}\n')

# Combine data into a new Excel file
master_file_path = r"C:\Users\MT1070\Desktop\Master Call Volume\output.xlsx"
final_sheet.to_excel(master_file_path, index=False)
# writer.save()


'''
# Export dataframe to an Excel file
excel_merged.to_excel('SpinSci_pilot_extract_eval.xlsx', index=False)

if file_names == 'xlsx':
        df = pd.read_excel(file.read(), engine='openpyxl')
        final_sheet = final_sheet.append(df, ignore_index=True)
    elif file_names == 'xls':
        df = pd.read_excel(file.read())
        final_sheet = final_sheet.append(df, ignore_index=True)
    elif file_names == 'csv':
        df = pd.read_csv(file.read())
        

'''