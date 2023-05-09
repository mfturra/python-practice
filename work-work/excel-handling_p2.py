import os
from openpyxl import Workbook

file_dir = "C:\\Users\\MT1070\\Mass General Brigham\\Digital Health Innovation - SpinSci - BWH - SpinSci - BWH\\6. Evaluation\\Pilot Data Extracts\\5.7.2023"

final_wb = Workbook()

for root, dir, filenames in os.walk(file_dir):
    for file in filenames:
        file_name = file.split('.')[0]

        # Absolute path for all joined excel files
        file_path = os.path.abspath(os.path.join(root,file))

        # Create new sheet in desired workbook
        final_wb.create_sheet(file_name)
        final_ws = final_wb[file_name]

final_wb.save("SpinSci_pilot_extract_eval.xlsx")
