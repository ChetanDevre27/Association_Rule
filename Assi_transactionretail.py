# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:01:37 2023

@author: chetandevre27
"""
#                           ASSIGNMENT 6 TransactionDetails.py

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
'''
problem statement:

A retail store in India, has its transaction data, and it would like to know the buying pattern of the 
consumers in its locality, you have been assigned this task to provide the manager with rules 
on how the placement of products needs to be there in shelves so that it can improve the buying
patterns of consumes and increase customer footfall. 


Objective:
    
    Maximize: 
        1. Increase store visits by strategically placing products for visibility and appeal.
        2. Optimize product layout to boost impulse buying and overall sales.
        3. Arrange complementary products for increased transaction value.
    
    Minimize:
        1.Enhance customer satisfaction by reducing time spent searching for products.
        2.Ensure consistent availability of popular products to avoid customer dissatisfaction.

    
Constraints:
    
    1. Optimize product placement within the available shelf space
    2. Implement changes within the allocated budget.
    3. Follow agreements with brands regarding specific product placement.
    4. Balance product placement to optimize inventory turnover.


Data Disctionary:
    
    
| Feature      | Data Type | Relevance to Model | Description                                       |
|--------------|-----------|---------------------|--------------------------------------------------|
| 'HANGING'    | Object    | High                | Type of product (e.g., 'LANTERN', 'COAT')        |
| 'HEART'      | Object    | High                | Product attribute (e.g., 'METAL', 'CREAM')       |
| 'HOLDER'     | Object    | High                | Type of product (e.g., 'WHITE', 'CUPID')         |
| 'T-LIGHT'    | Object    | Medium              | Type of product (e.g., 'HANGER', 'KNITTED')      |
| 'WHITE'      | Object    | Medium              | Product color (e.g., 'WHITE', 'RED')             |
| NA           | Object    | Low                 | Placeholder for missing values                   |

'''

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

# Imported required packages


import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

# Read the CSV file into a DataFrame.
trans = pd.read_csv('C:/1-python/Assi/transactions_retail1.csv')

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

trans.columns
'''
Features present in this are as follows:
    
''HANGING'', ''HEART'', ''HOLDER'', ''T-LIGHT'', ''WHITE'', 'NA'
'''

trans.shape
# it contains 557040 rows and 6  columns

trans.info()
# All columns are of Object Data type

trans.isna().sum()
# Except HANGING column all are containing the NULL value

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪


trans.fillna('0', inplace=True)
trans.isna().sum()
# So there is no null value 

trans.drop(['NA'],axis=1,inplace=True)
# We have dropped the Last column

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
# Convert the DataFrame to a list of transactions.
trans_list = trans.values.tolist()

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

# To generate association rules, we can directly use the 'trans_list.' 
# However, let's separate out each item from 'trans_list.'
all_trans_list = [i for item in trans_list for i in item]

# Now, we count the frequency of each item using the Counter function from the 
# collections package, and sort the frequencies in ascending order.
item_frequencies = Counter(all_trans_list)
item_frequencies = sorted(item_frequencies.items(), key=lambda x: x[1])

# Separate out items and their count.
items = list(reversed([i[0] for i in item_frequencies]))
frequencies = list(reversed([i[1] for i in item_frequencies]))

# Now, let's plot a bar graph of item frequencies.
plt.bar(height=frequencies[0:11], x=list(range(0, 11)))
plt.xticks(list(range(0, 11)), items[0:11])
plt.xlabel("Items")
plt.ylabel("Count")

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

# Now, we move on to association rule mining.

# Convert 'trans_list' to a DataFrame.
trans_series = pd.DataFrame(pd.Series(trans_list))

# Delete the last empty row.
trans_series = trans_series.iloc[:len(trans_list)-1, :]

# Rename the column as 'Transactions.'
trans_series.columns = ['Transactions']

# Perform one-hot encoding on the 'Transactions' column.
x = trans_series['Transactions'].str.join(sep='*')
x = x.str.get_dummies(sep='*')

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪

from mlxtend.frequent_patterns import apriori, association_rules
# Apply the Apriori algorithm with a minimum support of 0.0075.
frequent_itemsets = apriori(x, min_support=0.0075, max_len=4, use_colnames=True)

# Sort the frequent item sets by support values.
frequent_itemsets.sort_values('support', ascending=False, inplace=True)

# Generate association rules based on the frequent itemsets.
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Display the top 20 rules.
print(rules.head(20))

# Sort and display the top 10 rules based on lift.
print(rules.sort_values('lift', ascending=False).head(10))





























