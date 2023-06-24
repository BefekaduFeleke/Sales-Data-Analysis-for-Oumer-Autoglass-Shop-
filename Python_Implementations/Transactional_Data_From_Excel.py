import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel('C:/Users/befek/OneDrive/Desktop/Pythhh.xlsx')

# Sort the DataFrame by 'Customer Name' and 'Sale Date'
df = df.sort_values(by=['Customer Name', 'New_Date'])

# Create a new DataFrame to hold the merged transactions
merged_df = pd.DataFrame(columns=['Customer Name', 'Merged Product Codes', 'New_Date'])

# Initialize variables for tracking the current transaction
current_customer = ''
current_date = ''
merged_product_codes = ''

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Check if the current row is part of the same transaction
    if row['Customer Name'] == current_customer and row['New_Date'] == current_date:
        # Append the product code to the merged product codes
        merged_product_codes += ' ' + row['Product Code']
    else:
        # Add the previous transaction to the merged DataFrame, if any
        if current_customer != '':
            merged_df = pd.concat([merged_df, pd.DataFrame({'Customer Name': [current_customer],
                                                            'Merged Product Codes': [merged_product_codes],
                                                            'New_Date': [current_date]})],
                                  ignore_index=True)
        
        # Update the current transaction variables
        current_customer = row['Customer Name']
        current_date = row['New_Date']
        merged_product_codes = row['Product Code']

# Add the last transaction to the merged DataFrame
merged_df = pd.concat([merged_df, pd.DataFrame({'Customer Name': [current_customer],
                                                'Merged Product Codes': [merged_product_codes],
                                                'New_Date': [current_date]})],
                      ignore_index=True)

# Export the merged DataFrame to an Excel file
merged_df.to_excel('output_file3.xlsx', index=False)
