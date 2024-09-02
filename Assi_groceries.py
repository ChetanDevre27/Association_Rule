# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:01:37 2023

@author: chetandevre27
"""

#                               ASSIGNMENT
'''


Business Objective:
    
maximize: Identify and promote book combinations that are 
frequently purchased together to increase cross-selling opportunities.

Minimize: Increase sales and revenue by promoting popular book categories 

Constraints: The business needs to address online competition.
Strategies should include both online and offline components to capture a broader market.
'''

'''
DataFrame:

Nominal Data:

'ChildBks': Children's books category.
'YouthBks': Youth books category.
'CookBks': Cookbooks category.
'RefBks': Reference books category.
'ArtBks': Art books category.
'GeogBks': Geography books category.
'ItalCook': Italian Cookbooks category.
'ItalAtlas': Italian Atlases category.
'ItalArt': Italian Art books category.
'Florence': Possibly a location or specific book related to Florence.

'''

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('C:/1-python/Assi/book.csv')
df

#₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪₪
df.columns
###################################
df.shape
# the dataset contain 2000 rows and 11 columns
###################################
df.dtypes

######################################
a=pd.isnull(df)
a
a.sum()

#As there is no null value in the dataset

#####################################
q=df.value_counts()
####################################
# Five Number Summary
v=df.describe()
# The mean value is near to zero and also the standard deviation is a;dp
# near to zero and the meadian value for the all datapoints is zero
df.info()

'''
# This will give us the informationn about all the points
'''
####################################
# Visualization of Data

# 1. Check for the outlier

sns.boxplot(df,x='ChildBks')
# No outlier 
sns.boxplot(df,x='YouthBks')
#There is one outlier 
sns.boxplot(df,x='CookBks')
# No Outlier
sns.boxplot(df,x='RefBks')
# There is one outlier
sns.boxplot(df)
# Observe that some columns contain  the outlier so we have to normalize it

#2. Pairplot
sns.pairplot(df)
# No Datapoints are corelated as the all the datapoints are in scatter form 

#3. Heatmap
corr=df.corr()
sns.heatmap(corr)
# The diagonal color of the heatmap is same as the datapoints folllow some pattern
# so we can use this data for the model building
############################################
#Normalization
#The data is numeric one so we have to perform normalization

def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_fun(v)
df_norm

b=df_norm.describe()

sns.boxplot(df_norm)
# No Outlier is remaining
# The all the quantile points are converted in the rande of 0-1
############################################
# Model Building
# Association Rules
pip install mlxtend
from mlxtend.frequent_patterns import apriori,association_rules


data=pd.read_csv('C:/1-python/Assi/book.csv')
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

# Visualize the rules
import networkx as nx
import matplotlib.pyplot as plt

# Create directed graph from the rules
G = nx.from_pandas_edgelist(rules, 'antecedents', 'consequents')

# Draw the graph
fig, ax = plt.subplots(figsize=(14, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, alpha=0.7)
plt.title("Association Rules Network", fontsize=15)
plt.show()

###################################################

# the benefits/impact of the solution 
# By identifying books that are frequently purchased together,
# the bookstore can create curated bundles or recommendations, enhancing the overall 
# shopping experience for customers.
# By using this association rule we can stratergically placed the books together to encourage
# the customer to purchased more items which will help to increased the overall revenue

