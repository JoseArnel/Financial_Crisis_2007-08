

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

# ex: Scatterplots, pg 34
ax = telecom.plot.scatter(x='T', y='VZ', figsize=(4,4), marker='$\u25EF$')
ax.set_xlabel('ATT (T')
ax.set_ylabel('Verizon (VZ)')
ax.axhline(0, color='grey', lw=1)
ax.axvline(0, color='grey', lw=1)

#ex: Histogram of Annual Incomes of 1,000 laon applicants
import pandas as pd
import seaborn as sns

sample_data = pd.DataFrame({
    'income': loans_income.sample(1000),
    'type': 'Data',
})
sample_mean_05 = pd.DataFrame({
    'income' : [laons_income.sample(5).mean() for _ in range(1000)],
    'type' : 'Mean of 5',
})
sample_mean_20 = pd.DataFrame({
    'income' :[loans_income.sample(20).mean() for _ in range(1000)],
    'type' : 'Mean of 20',
})
results = pd.concat([sample_data, sample_mean_05, sample_mean_20])
g = sns.FacetGrid(results, col='type', col_wrap=1, height=2, aspect=2)
g.map(plt.hist,'income', range[0,20000], bins=40)
g.set_axis_laels('Income', 'Count')
g.set_titles('{col_name}')
