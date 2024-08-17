

# ex: Variability Estimates of State Population, Chp1 Exploratory Data Analysis, pg 18
state['Population'].std()
state['Population'].quantile(0.75).state['Population'].quantile(0.25)
robust.scale.mad(state['Population'])# robust.scale frm statsmodels package.

# ex: Frequency Tables and Histograms, pg 22
binnedPopulation = pd.cut(state['Population'], 10)
binnedPopulation.value_counts()
#matplot visualization
ax = (state['Population'] / 1_000_000).plot.hist(figsize=(4, 4))
ax.set_xlabel('Population (millions)')

#ex: Exploring Binary and Categorical Data pg 27
ax = dfw.transpose().plot.bar(figsize=(4,4), legend=False)
ax.set_xlabel('Cause of delay')
ax.set_ylabel('Count')

#ex: Correlation, pg 32
etfs = sp500_px.loc[sp500_px.index > '2012-07-01', sp500_sym[sp500_sym['sector'] == 'etf'] ['symbol']]
#seaborn.heatmap package
sns.heatmap(etfs.corr(), vmin=-1, vmax=1), cmap=sns.diverging_palette(20, 220, as_cmap=True)