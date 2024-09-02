# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:01:37 2023

@author: yuvra_d0x8avj
"""

'''
Problem Statement: 
    
The Departmental Store, has gathered the data of the products it sells on a Daily basis.
Using Association Rules concepts, provide the insights on the rules and the plots.


Objective:
    
Promote product combinations to increase cross-selling.
Recommend frequently bought together products for a better shopping experience.
Predict demand and optimize stock for often co-purchased items. Analyze less-associated products to cut stock levels and minimize waste.

Constraint:
    
Implement changes seamlessly without disrupting daily tasks.
Manage implementation costs within budget constraints.


Data Dictionary:
    
| Feature            | Data Type    | Relevance to Model  | Description                                                |
|--------------------|--------------|---------------------|------------------------------------------------------------|
| citrus fruit       | Categorical  | Important           | Presence or absence of citrus fruit in the shopping basket |
| semi-finished bread| Categorical  | Moderate            | Presence or absence of semi-finished bread in the basket   |
| margarine          | Categorical  | Moderate            | Presence or absence of margarine in the shopping basket    |
| ready soups        | Categorical  | Low                 | Presence or absence of ready soups in the shopping basket  |

'''
# import all the libraries

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from mlxtend.frequent_patterns import apriori, association_rules

#--------------------------------------------------------------------


# In this script, we aim to perform association rule mining on transactional data 
# in the 'groceries.csv' file. Since the data is unstructured and the size of 
# each row is not uniform, we use the open() function to read the file and 
# create a list called 'groceries.'

groceries = []
with open("groceries.csv") as f:
    groceries = f.read()


# Next, we split the data into separate transactions using a comma as the separator.
# The transactions are then stored in the 'groceries_list' variable.
groceries = groceries.split("\n")
groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))

# To generate association rules, we can directly use the 'groceries_list.' 
# However, let's separate out each item from 'groceries_list.'
all_groceries_list = [i for item in groceries_list for i in item]

# Now, we count the frequency of each item using the Counter function from the 
# collections package, and sort the frequencies in ascending order.

item_frequencies = Counter(all_groceries_list)
item_frequencies = sorted(item_frequencies.items(), key=lambda x: x[1])

# Separate out items and their count.
items = list(reversed([i[0] for i in item_frequencies]))
frequencies = list(reversed([i[1] for i in item_frequencies]))

# Now, let's plot a bar graph of item frequencies.

plt.bar(height=frequencies[0:11], x=list(range(0, 11)))
plt.xticks(list(range(0, 11)), items[0:11])
plt.xlabel("Items")
plt.ylabel("Count")

# Now, we move on to association rule mining.
#-------------------------------------------------------------------

# Convert 'groceries_list' to a DataFrame.
groceries_series = pd.DataFrame(pd.Series(groceries_list))

# Delete the last empty row.
groceries_series = groceries_series.iloc[:9835, :]

# Rename the column as 'Transactions.'
groceries_series.columns = ['Transactions']

# Perform one-hot encoding on the 'Transactions' column.
x = groceries_series['Transactions'].str.join(sep='*')
x = x.str.get_dummies(sep='*')

#--------------------------------------------------------------------

# Apply the Apriori algorithm with a minimum support of 0.0075.
frequent_itemsets = apriori(x, min_support=0.0075, max_len=4, use_colnames=True)

# Sort the frequent item sets by support values.
frequent_itemsets.sort_values('support', ascending=False, inplace=True)

# Generate association rules based on the frequent itemsets.
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1)

# Display the top 20 rules.
rules.head(20)

# Sort and display the top 10 rules based on lift.
rules.sort_values('lift', ascending=False).head(10)
