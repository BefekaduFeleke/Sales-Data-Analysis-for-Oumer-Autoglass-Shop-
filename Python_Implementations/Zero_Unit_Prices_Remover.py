import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('C:/Users/befek/OneDrive/Desktop/merged_file.xlsx')

# Delete rows where the unit price is zero
df = df[df['Unit Price'] != 0]

# Save the modified DataFrame back to a new Excel file
df.to_excel('C:/Users/befek/OneDrive/Desktop/Unit_Yewetalet_file.xlsx', index=False)
