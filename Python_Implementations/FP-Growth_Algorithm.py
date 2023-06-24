import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpmax, association_rules

# Read the transactional data from Excel
df = pd.read_excel('output_file3.xlsx')

# Split the merged product codes into lists of individual items
transactions = df['Merged Product Codes'].str.split()

# Encode the transactions into a transaction matrix
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
encoded_df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply FP-Growth algorithm to discover frequent itemsets
frequent_itemsets = fpmax(encoded_df, min_support=0.003, use_colnames=True)

# Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.1, support_only=True)

# Adjust the display options
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Print the generated association rules
output_rules = rules[['antecedents', 'consequents', 'confidence', 'support']]
print(output_rules)

