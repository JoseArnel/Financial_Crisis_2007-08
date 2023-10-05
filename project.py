import pandas_datareader.data as wb
import pandas as pd
import numpy as np
import datetime 
import os 
import yfinance as yfin

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

# double check C

# Exploratory Data Analysis of stock prices, to practice visualizationas, python, and external libraries such as; Pandas, Matplot, Seaborn, Numpy
# This project focuses on American Bank Stocks during the 2008-2009 Economic Crash, to see how they they progress and recovered from the Financial Crisis
# to more recent dates of the early 2016 

########
# DATA #
########
start = "2006-01-01" # date range 
end = "2016-01-01"
#Tickers for Each Bank: Bank of America - BAC , CitiGroup - C, Goldman Sachs - GS , JPMorgan Chase - JPM, Morgan Stanley MS, Wells Fargo - WFC
yfin.pdr_override()
# Bank of America
BAC = wb.get_data_yahoo('BAC', start, end)
# CitiGroup
C = wb.DataReader('C', start, end)
# Goldman Sachs
GS = wb.DataReader('GS', start, end)
# JPMorgan Chase
JPM =wb.DataReader('JPM', start, end)
# Morgan Stanley 
MS = wb.DataReader('MS', start, end)
# Wells Fargo 
WFC = wb.DataReader('WFC', start, end)
# print(C.head())

tickers = ['BAC', 'C', 'GS', 'JPM', 'MS', 'WFC']
# print(tickers)

# help(pd.concat)
# CONCANTENATE the Bank Dataframes 
bank_stocks = pd.concat([BAC, C, GS, JPM, MS, WFC], axis = 1, keys=tickers) # axis 1 cause concat with columns.
# print(bank_stocks)

# SET column name levels
bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']
print(bank_stocks.head())

#######
# EDA #
####### exploratory data analysis
# resources: 
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.xs.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html

# max Close price for each bank stock throughout, time periods
max = bank_stocks.xs(key='Close', level='Stock Info', axis=1).max()
# print(max)

# new empty DataFrame 
returns = pd.DataFrame()

# pct_change() on Close column to create return values 
# create column represent returns for each bank stocks
def pairplot():
    for tick in tickers:
        # returns[tick + " Returns"] = (bank_stocks.xs(tick, level='Bank Ticker', axis = 1)).pct_change()
        # print(bank_stocks.xs('BAC', level = 'Bank Ticker', axis = 1).pct_change())
        returns[tick + " Returns"] = bank_stocks[tick]['Close'].pct_change()
    print(returns)
    # pairplot of returns df
    sns.pairplot(data = returns[1:])
    #analysis: MS is the lowest, JPM & WFC seem to be the highest, C & HS slightly simlar 

# dates each bank stocks had the best and worst single day return 
# best single day return
rmax = returns.idxmax()
#analysis: 2009-01-20 - Barack Obama Inauguration, 4 banks returned same day of worst day
# print(rmax)

# worst single day return
rmin = returns.idxmin()
#analysis: Morgan lost 80% of its market, 42% slide in its share price in 2 days, JP Morgans next day is better 
# print(rmin)

# the lower the std, the MORE CLUSTERED the distribution towards mean (more reliable)
# the higher the std, the MORE SPREAD out the distribution (the more riskier)
# STANDARD DEVIATIONS of returns (which is the riskiest)
rstd = returns.std()
#analysis: the riskiest stock is C & the least riskiest is GS
print(returns.std())

# std for year 2015
rstd_2015 = returns.loc['2015-01-03':'2015-12-31'].std()
#analysis: the riskiest in 2015 was MS and least riskiest in 2015 was WFC
# print(rstd_2015)

# plot for Close Price for each bank 
def lineplot():
    # using xs instead
    # bank_stocks.xs(key = 'Close', level='Stock Info', axis = 1).plot()
    for ticks in tickers:
        bank_stocks[ticks]['Close'].plot(label = ticks, figsize=(12,4))
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("10 Year Closing Prices of American Banks")
    plt.show()
lineplot()

def distplot():
    # DISTPLOT using seaborn, for Morgan Stanley's 2015 returns
    sns.distplot(returns.loc['2015-01-01':'2015-12-31']['MS Returns'], color = 'green', bins=100)
    #analysis: MS seems to be fairly distributed in 2015

    # DISTPLOT using seaborn, for CitiGroup's 2008 returns
    sns.distplot(returns['2008-01-01': '2008-12-31']['C Returns'], color = 'red', bins = 50)
    #analysis: This was the during the Collapse of CitiGroup where the stock had dropped 76% (second worst drop in terms of banks)
    #further shown in the chart where it depicts high volatility within the year
# distplot()

##################
# Visualizations #
##################
# calculating MOVING AVERAGES 
# 30 day average of Bank of America's Close Price stock for 2008
def moving_avg(): #favourite
    # BACma = BAC.loc['2008-01-01': '2008-12-30']['Close'].rolling(30).mean()
    # BACma.plot(label='30 Day Mov')
    plt.figure(figsize = (12,4))
    BAC.loc['2008-01-01':'2009-01-01']['Close'].rolling(window=30).mean().plot(label='30Day Moving Avg')
    BAC.loc['2008-01-01':'2009-01-01']['Close'].plot(label='BAC CLOSE PRICE')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title("Bank of America's 08 Close Price v. 30Day Moving Avg")
    plt.show()
# moving_avg()

def heatmap():
    corr = bank_stocks.xs(key = 'Close', level = 'Stock Info', axis = 1).corr()
    sns.heatmap(corr, annot = True)
# heatmap()

def clustermap(): # run time error
    sns.clustermap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)
# clustermap()

# Jose Arnel Manipon
# TO DO, Clean up Graphs and Each title
