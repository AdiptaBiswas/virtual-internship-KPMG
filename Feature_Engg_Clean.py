#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date


WBK = 'KPMG_Data.xlsx'
Book = pd.read_excel(WBK, sheet_name=None)
print(Book.keys())


Demo_DF = pd.read_excel(WBK, sheet_name="CustomerDemographic")
Addr_DF= pd.read_excel(WBK, sheet_name="CustomerAddress")
Tranx_DF= pd.read_excel(WBK, sheet_name="Transactions")
New_Cust_DF = pd.read_excel(WBK, sheet_name="NewCustomerList")
Demo_DF.head(3)


def col_name_format(*df):
    DF_ls = []
    for c in df:
        new_col = c.iloc[0]
        c = c[1:]
        c.columns = new_col
        DF_ls.append(c)
    return DF_ls


Demo_DF, Addr_DF, Tranx_DF, New_Cust_DF = col_name_format(Demo_DF, Addr_DF, Tranx_DF, New_Cust_DF)


Demo_DF = Demo_DF.merge(Addr_DF, how = "left", on="customer_id")
Demo_DF.where(Demo_DF.notnull(), np.nan)


def nan_pcent(df):
    points = df.shape[0]
    for col in df.columns:
        print("* {} has {}% nan values\n".format(col,((df[col].isna().sum())/points)*100))


print("Demo_DF shape: {}".format(Demo_DF.shape))
print()
nan_pcent(Demo_DF)


Demo_DF.drop(columns=["first_name", "last_name", "default", "deceased_indicator", "address", "country"], inplace=True)


Demo_DF["gender"] = Demo_DF["gender"].apply(lambda x: "Female" if x=="F" else "Female" if x=="Femal" else "Male" 
                                            if x=="M" else "NA")


print(list(set(Demo_DF["gender"])))

def age_calculation(dob):
    dob = pd.to_datetime(dob)
    today = date.today()
    return (today.year - 3) - dob.year

Demo_DF['Age'] = Demo_DF['DOB'].apply(age_calculation)
Demo_DF['Age'] = Demo_DF['Age'].replace(np.nan, "NA")
Demo_DF['Age'] = Demo_DF['Age'].apply(lambda x: int(x) if isinstance(x, float) else "NA")
print(set(Demo_DF["Age"].to_list()))


Demo_DF.drop(columns="DOB",inplace=True)


print("Tranx_DF shape: {}".format(Tranx_DF.shape))
print()
nan_pcent(Tranx_DF)


Tranx_DF.drop(columns=["transaction_date", "online_order", "order_status", "product_id", "transaction_id", 
                       "list_price", "standard_cost", "product_first_sold_date"], inplace=True)


Tranx_DF.head()


def prod_class(*trnx_df):
    df = Tranx_DF
    for column in trnx_df:
        print("Col \'{}\' items: {}".format(column, set(df[column].to_list())))
        print()
                 
prod_class("brand", "product_line", "product_class", "product_size")


Demo_DF_old = Demo_DF


New_Cust_DF['Age'] = New_Cust_DF['DOB'].apply(age_calculation)
New_Cust_DF['Age'] = New_Cust_DF['Age'].replace(np.nan, "NA")
New_Cust_DF['Age'] = New_Cust_DF['Age'].apply(lambda x: int(x) if isinstance(x, float) else "NA")
print(set(New_Cust_DF["Age"].to_list()))


print([col for col in New_Cust_DF.columns.to_list()])

print()
New_Cust_DF = New_Cust_DF.loc[:, New_Cust_DF.columns.notnull()]


New_Cust_DF["customer_id"] = [Demo_DF.shape[0]+1+i for i in range(len(New_Cust_DF))]


New_Cust_DF = New_Cust_DF[[col for col in Demo_DF.columns.to_list()]]


New_Cust_DF = Demo_DF.append(New_Cust_DF, ignore_index = True)


New_Cust_DF


Demo_DF_old = Demo_DF_old.merge(Tranx_DF, how="inner", on="customer_id")

Demo_DF_old.head()

# *By:*  `Adipta Biwas`
