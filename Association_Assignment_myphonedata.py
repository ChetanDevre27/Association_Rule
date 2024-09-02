# -*- coding: utf-8 -*-
'''
Business Objective:
    
    maximize:
        
        1. Place high-demand items prominently.
        2. Analyze traffic patterns to position products effectively.
        3. Group complementary products to encourage additional purchases.
        4. Rotate placements based on seasons and trends.
        5. Designate areas for small, enticing items near checkout.
        6. Ensure a well-organized, spacious, and welcoming store layout.
        
    Minimize:
        
        1. Regularly restock to avoid empty shelves.
        2. Organize the store logically with clear signage.
        3. Keep shelves uncluttered to aid easy product discovery.
        4. Ensure adequate lighting to showcase products.
        5. Streamline the checkout process to minimize wait times.
    

Cobnstrains:
            Space limitations
            Product category restrictions
            Cultural sensitivity
            Budgetary constraints
            Existing store infrastructure
            Customer privacy
            Maintain accessibility
            Address seasonal variations
'''

'''
Dataframe:

| Feature       | Data Type   | Relevance to Model   | Description                                      |
|------------|-------------|----------------------|--------------------------------------------------|
| Red        | Categorical | Yes                  | Preference for the color red (1: liked, 0: not liked) |
| White      | Categorical | Yes                  | Preference for the color white (1: liked, 0: not liked) |
| Green      | Categorical | Yes                  | Preference for the color green (1: liked, 0: not liked) |
| Yellow     | Categorical | Yes                  | Preference for the color yellow (1: liked, 0: not liked) |
| Orange     | Categorical | Yes                  | Preference for the color orange (1: liked, 0: not liked) |
| Blue       | Categorical | Yes                  | Preference for the color blue (1: liked, 0: not liked) |
'''

#---------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('myphonedata.csv')
df

#---------------------------------------------------------------------

df.columns
'''
['red', 'white', 'green', 'yellow', 'orange', 'blue']
'''
#---------------------------------------------------------------------

df.head()
# It will show thw first five rows of the data

#---------------------------------------------------------------------

df.shape
# The dataset contain 11 rows and 6 columns

#---------------------------------------------------------------------

a=df.describe()
# The mean is near to zero and the mean and median diffrence is also not very
# big . The standard deviation is also near to zero
# so  we can say that the datapoints are scatter near the mradian

#---------------------------------------------------------------------

df.info()
# All columns are of integer datatype
 
#---------------------------------------------------------------------
df.dtypes
# The datatype of all columns is of numeric type so no need of encoding technique

#---------------------------------------------------------------------

# Find the missing values
df.isnull().sum()
# There is no null  value in the daaset

#---------------------------------------------------------------------

# Visualize the dataset

#Plot the boxplot for the outlier analysis
sns.boxplot(df,x='red')
# No outlier 

sns.boxplot(df,x='white')
# No outlier

sns.boxplot(df,x='green')
# One outlier is present

sns.boxplot(df,x='yellow')
# One outlier present

sns.boxplot(df)
# There is three columns which contain the outliers 

# Plot a pairplot to understand the relationship between columns
sns.pairplot(df)
# The graphs does not show any relation as the datapoints are in scatter form

# To know more plot the heatmap
corr=df.corr()
sns.heatmap(corr)
# The heatmap showing some pattern of  the datapoins

#---------------------------------------------------------------------

#  As there is outliers present in the dataset so we normalize it using normalization technque


def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(a)
df_norm
# The mean and median diffrence is in the range of 0-1 and the standard deviation
# is also near to zero


b=df_norm.describe()

sns.boxplot(df_norm)
# No Outlier is remaining
# The all the quantile points are converted in the rande of 0-1

#---------------------------------------------------------------------


# Model Building
# Association Rules
from mlxtend.frequent_patterns import apriori,association_rules

data=pd.read_csv('myphonedata.csv')
data

# All the data is in properly separated form so no need to apply the encoding techique
# as it is already is in the form of numeric one

from collections import Counter
item_frequencies=Counter(data)

# Apriori algorithm
frequent_itemsets = apriori(data, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

# This generate association rule for columns
# comprises of antescends,consequences

rules.head(20)
rules.sort_values('lift',ascending=False).head(10)


#---------------------------------------------------------------------

# By using this data we can suggest to the customer which colour he/she
# should select for the mobile 
