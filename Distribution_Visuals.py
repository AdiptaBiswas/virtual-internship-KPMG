#!/usr/bin/env python
# coding: utf-8

# ### Package

# import pandas as pd
# import numpy as np
# import numpy as np, pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# ### Data 

# `old_cust_df`  is a **merged** dataframe containing *customer demographic*, *customer transactions* and *customer address* data-sets
# 
# `new_cust_df`  is a **merged** dataframe containing old and new *customer demographic* and *customer address* data-sets

# old_cust_df = pd.read_csv("C:\\Users\\ADIPTA BISWAS\\Downloads\\Customer_Details_Old_Final.csv")
# new_cust_df = pd.read_csv("C:\\Users\\ADIPTA BISWAS\\Downloads\\Customer_DF_Final.csv")

# old_cust_df.drop(columns="Unnamed: 0", inplace=True)
# new_cust_df.drop(columns="Unnamed: 0", inplace=True)

# print("Dimension of {}: {}".format("old_cust_df", old_cust_df.shape))
# print()
# old_cust_df.head()

# print("Dimension of {}: {}".format("new_cust_df", new_cust_df.shape))
# print()
# new_cust_df.head()

# ### Distributions and Plots 

# ####  Ages histogram 

fig = plt.figure(figsize = (8,6))
axes = fig.gca()
new_cust_df.hist('Age', bins=55, ax=axes, color='#0504ca', rwidth=0.85, alpha=0.8);
plt.title('Age Distribution', fontsize = 15);
plt.xlabel('Age', fontsize = 15);
plt.ylabel('Number of customers', fontsize = 15)
plt.tight_layout()

# **Observations**: 
# 
# * Customers under the age group `35 - 45` are the majority in the distribution
# * Customers under the age group `63 - 85` are the least.
# * There is an outlier at `174` and that's an incorrect input of data
# * The Median age is estimated to be around `43 - 45`
# * The distribution is a bit *Right Skewed*

# #### Number of customers vs. Gender 

plt.figure(figsize=[6,4])
sns.countplot(x='gender', data=new_cust_df);
plt.title('Distribution of Gender', fontsize = 15);
plt.xlabel('Gender', fontsize = 15);
plt.ylabel('Number of customers', fontsize = 15)
plt.tight_layout()

# **Observations**: 
# 
# * As per the data being provided, it is seen that there are a greater number of `Females` than other genders
# * The label `U` denotes the `Unknown` gender class

# #### Coverage of Gender on Age Distribution

plt.figure(figsize=[8,4])
plt.hist('Age', data=new_cust_df[new_cust_df['gender'] == 'Male'], alpha=0.5, label='Male', color = '#0504aa',
        rwidth = 0.8);
plt.hist('Age', data=new_cust_df[new_cust_df['gender'] == 'Female'], alpha=0.5, label='Female',
        rwidth = 0.8);
plt.title('Age and Gender Distribution', fontsize = 15);
plt.xlabel('Age', fontsize = 15);
plt.legend();

# **Observations**: 
# 
# * The `Males` are seen to be younger in this data 
# * The majority of `Females` fall in the middle and majority of the distribution
# * Number of aged `Females` are more than the aged `Males`

def Plots(x, color, title, xlab, ylab, *size):
    plt.figure(figsize=size)
    sns.countplot(x=x, data=new_cust_df, color = color);
    plt.title(title, fontsize = 15);
    plt.xlabel(xlab, fontsize = 15);
    plt.ylabel(ylab, fontsize = 15)
    plt.tight_layout()

# #### Wealth Segment 

Plots("wealth_segment","deeppink","Wealth Class Distribution","Wealth Class","Number of customers",6,4)

# **Observations**: 
# 
# * There are a major number of customers under `Mass Customer` followed by `High New Worth Customers`
# * The number of customers under `Affleunt Customers` and `High New Worth Customers` are almost equal

# #### Job Industry

Plots("job_industry_category","orange","Job Industry Distribution","Industry","Number of customers",13,4)


# **Observations**: 
# 
# * There are a major number of customers under `Manufacturing` and `Financial Services` followed by `Health`
# * The number of customers under `Telecommunications` followed by `Agriculture` are the least

# #### State Distribution

Plots("state","lime","State Distribution","State","Number of customers",6,4)

# **Observations**: 
# 
# * There are a major number of customers from `NSW` in the data
# * The number of customers from `Victoria` and `New South Wales` are the least

fig = plt.figure(figsize = (6,4))
axes = fig.gca()
new_cust_df.hist('property_valuation', bins=7, ax=axes, color='deepskyblue', rwidth=0.85, alpha=1);
plt.title('Property Valuation Distribution', fontsize = 15);
plt.xlabel('Property Valuation', fontsize = 15);
plt.ylabel('Number of customers', fontsize = 15)
plt.tight_layout()

# **Observations**: 
# 
# * Majority of the customers in the data have a `property valuation` ranging between `7 - 8`
# * `Property valuation` between  `4 - 6` are the least
# * The distribution is *left skewed*

# #### Customers having cars? 

plt.figure(figsize=[6,4])
sns.countplot(x='owns_car', data=new_cust_df);
plt.title('Customers having cars', fontsize = 15);
plt.xlabel('Car owners', fontsize = 15);
plt.ylabel('Number of customers', fontsize = 15)
plt.tight_layout()
