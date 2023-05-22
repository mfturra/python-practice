# Import required modules
import pandas as pd


# Specify paths to files
path = r'C:\Users\MT1070\Desktop\Master Call Volume\SpinSci Call Volume Evaluation.xlsx'

# Read file and skip the first row
df = pd.read_excel(path, skiprows=[0])

# Drop empty rows
df = df.dropna()

# List of column names and operation for data handling
agg_functions = {'total_internal_calls':'sum', 'total_external_calls':'sum', 
                 'total_english_calls':'sum', 'total_spanish_calls':'sum', 'total_option1_selected':'sum',
                 'total_option2_selected':'sum', 'total_option3_selected':'sum', 'total_option4_selected':'sum',
                 'total_option5_selected':'sum', 'total_unique_calls':'sum', 'total_calls_transfered':'sum',
                 'total_calls_during_non_peak':'sum', 'total_calls_during_peak':'sum'}

# Drop repeated column rows
print(df['date'] == 'date')
# index_repeat = df[(df['date'] == 'datetotal')]

drop_repeat = df['date'] == 'date'
# df.drop(index_repeat, inplace=True)
# df.head(15)

# print(list(df.columns))
# print(df['date'])
# print(f'Column names are {df.columns}')
# df_new = df.groupby('date')

df_new = df.groupby(df['date'], sort=False).aggregate(agg_functions).reset_index() # Keep
# print(df_new)

# df_new.to_excel(path, sheet_name='Cleaner Data', index=False) # Keep















