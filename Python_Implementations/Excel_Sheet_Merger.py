import pandas as pd

# Generate a list of sheet names from 'Sheet1' to 'Sheet209'
sheet_names = [f'Sheet{i}' for i in range(1, 210)]

# Path to the Excel file
excel_file = 'C:/Users/befek/OneDrive/Desktop/Unmerged.xlsx'  # Replace with your file path

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate over each sheet and merge the data
for sheet_name in sheet_names:
    try:
        # Read the sheet into a DataFrame
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        
        # Append the DataFrame to the merged_data DataFrame
        merged_data = pd.concat([merged_data, df], ignore_index=True)
    except Exception as e:
        # Handle any exceptions (e.g., if a sheet doesn't exist)
        print(f"Error reading sheet '{sheet_name}': {str(e)}")

# Export the merged data to a new Excel file
merged_file = 'C:/Users/befek/OneDrive/Desktop/merged_file.xlsx'  # Replace with your file path
merged_data.to_excel(merged_file, index=False)

print("Sheets merged successfully.")
