# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
# create Data Frame
pd.DataFrame({"Name" : ['vivek', 'darshan', 'chirag', 'manish'],
                         "Age" : [22, 21, 21, 21],
                         "Phone":[9537318019, 9099441250, 6352451526, 9898653526]})


# %%
# Data Frmae With Row Lables
pd.DataFrame({"Name" : ['vivek', 'darshan', 'chirag', 'manish'],
                         "Age" : [22, 21, 21, 21],
                         "Phone":[9537318019, 9099441250, 6352451526, 9898653526]}, index=['user1', 'user2', 'user3', 'user4'])


# %%
# Series
pd.Series([60, 40, 90, 20])


# %%
# Series with Name
pd.Series([50, 30, 60, 80], name="Product_sales")


# %%
# Series with lables
pd.Series([50, 30, 50, 40], index=['apple', 'cherry', 'banana', 'mengo'], name='Fruite_sales_2020')


# %%
# Reading Files
# create DataFrame From file
productSalesReport = pd.read_csv('./sample_data/1000_Sales_Records.csv')


# %%
# Get The Length of dataFrame
productSalesReport.shape


# %%
# df.head() display first five row of dataframe
productSalesReport.head()


# %%
# we can use the csv index as our df index as well

productSalesReport = pd.read_csv('sample_data/1000_Sales_Records.csv', index_col=0)
productSalesReport.head()


# %%
# store data frame to csv
productSalesReport.to_csv('test.csv')


# %%
# accessing column from data frame

productSalesReport['Item Type']


# %%
# access specific cell of csv using dataframe index
productSalesReport['Item Type'][1]


# %%
# Index based selection


# %%
productSalesReport.iloc[0] 


# %%
# all columan, 5th row selection
productSalesReport.iloc[4,:]


# %%
# all rows, oth column
productSalesReport.iloc[:, 0]


# %%
# select first 3 rows with all column
productSalesReport.iloc[:3, :]


# %%
# select first 3 rows with last 3 columns
productSalesReport.iloc[:3, -3:]


# %%
# we can pass list as well
# select only 0th and 5th columns only with firdt 50 rows
productSalesReport.iloc[5, [0, 5]]


# %%
# select only 10th and 100th row with all column
productSalesReport.iloc[[10, 100], :]


# %%
# Lable based selection


# %%
# row index matters here, not actula position of data
# get the row which has index 1
productSalesReport.loc[1]


# %%
# select first five row and only include [Unit Price, Item Type, Region] columns
productSalesReport.loc[:5, ['Unit Price', 'Item Type','Region']]


# %%
# Conditional selection
# it is like asking quetions and getting result from static data


# %%
# select only Asia Region
productSalesReport.loc[productSalesReport.Region == 'Asia']


# %%
# get all the iteams which region is Asia and has lessthen 10K profit
productSalesReport.loc[ (productSalesReport.Region == 'Asia') & (productSalesReport['Total Profit'] <= 10000)]


# %%
# get all the iteams which Country is Nepal or Bhutan and has greater then 50K profit
productSalesReport.loc[(productSalesReport.Country.isin(['Nepal', 'Bhutan'])) & (productSalesReport['Total Profit'] >= 50000)]

# above query can be solved othjer way as well 
# productSalesReport.loc[( (productSalesReport.Country == 'Nepal') | (productSalesReport.Country == 'Bhutan')) & (productSalesReport['Total Profit'] >= 50000)]


# %%
# get all record which total profit is null
productSalesReport.loc[productSalesReport['Total Profit'].isnull()]


