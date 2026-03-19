# =========================
# PART 1 - PROBABILITY
# =========================

# Joint Probability
PO = 400
Total = 2000

K = round(PO / Total, 4)
print('Joint probability:', K)


# Conditional Probability
P1 = (400 / 2000) / (500 / 2000)
print('P(Actually placed order | Planned):', round(P1, 4))


# =========================
# BINOMIAL DISTRIBUTION
# =========================

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

p = 0.05
n = 10
k = np.arange(0, 11)

binomial = stats.binom.pmf(k, n, p)

print("P(X=0):", round(binomial[0], 4))
print("P(X=1):", round(binomial[1], 4))

cumbinomial = stats.binom.cdf(k, n, p)

print("P(X<=2):", round(cumbinomial[2], 4))
print("P(X>=3):", round(1 - cumbinomial[2], 4))


# =========================
# POISSON DISTRIBUTION
# =========================

rate = 3
n = np.arange(0, 16)

cumpoisson = stats.poisson.cdf(n, rate)

P_some = 1 - cumpoisson[0]
print("P(X>=1):", round(P_some, 4))

P_range = cumpoisson[4] - cumpoisson[1]
print("P(2<=X<5):", round(P_range, 4))

plt.plot(n, cumpoisson, 'o-')
plt.title('Poisson CDF')
plt.xlabel('X')
plt.ylabel('CDF')
plt.show()


# =========================
# BINOMIAL MANUAL
# =========================

from math import factorial as f

p = 0.868

P_X3 = f(3)/(f(3)*f(0)) * (p**3)
P_X0 = f(3)/(f(0)*f(3)) * ((1-p)**3)
P_X2 = f(3)/(f(2)*f(1)) * (p**2) * (1-p)

print("P(X=3):", P_X3)
print("P(X=0):", P_X0)
print("P(X>=2):", P_X2 + P_X3)


# =========================
# PART 2 - EDA
# =========================

import pandas as pd
import re
import plotly.express as px

# Load data
Basket = pd.read_csv("Basketball.csv")

# Clean up string entries
Basket = Basket.replace('-', 0)
Basket = Basket.replace(to_replace='to', value='-', regex=True)
Basket = Basket.replace(to_replace='_', value='-', regex=True)
Basket = Basket.replace(to_replace='~', value='-', regex=True)

# Extract year from TeamLaunch column
for i in range(len(Basket['TeamLaunch'])):
    x = str(Basket.loc[i, "TeamLaunch"])
    temp = re.findall(r'\d{4}', x)
    if temp:  # make sure a year was found
        Basket.loc[i, "TeamLaunch"] = int(temp[0])
    else:
        Basket.loc[i, "TeamLaunch"] = 0

# Ensure numeric columns are int or float
numeric_cols = ['TeamLaunch', 'PlayedGames', 'WonGames', 'Tournament', 'TournamentChampion']
for col in numeric_cols:
    Basket[col] = pd.to_numeric(Basket[col], errors='coerce').fillna(0).astype(int)

# Create additional metrics
Basket['Age'] = 2019 - Basket['TeamLaunch']
Basket['WinRate'] = Basket['WonGames'] / Basket['PlayedGames'].replace(0, 1)
Basket['ChampRate'] = Basket['TournamentChampion'] / Basket['Tournament'].replace(0, 1)

# Top & Low Teams
top_win = Basket.sort_values(by='WinRate', ascending=False).head(10)
low_win = Basket.sort_values(by='WinRate').head(10)

young = Basket.sort_values(by='Age').head(10)
old = Basket.sort_values(by='Age', ascending=False).head(10)

print("Top 10 Teams by WinRate:\n", top_win[['Team','WinRate']])
print("Bottom 10 Teams by WinRate:\n", low_win[['Team','WinRate']])

# =========================
# Visualizations
# =========================

# Scatter: Team vs WinRate colored by Age
px.scatter(Basket, x="Team", y="WinRate", color='Age', title="Team vs WinRate by Age").show()

# Scatter: PlayedGames vs WonGames
px.scatter(Basket, x="PlayedGames", y="WonGames", title="Games Played vs Games Won").show()

# Boxplot: Age
px.box(Basket, y='Age', title="Team Ages Distribution").show()

# Histogram: Age
px.histogram(Basket, x='Age', title="Histogram of Team Ages").show()

# =========================
# Correlation
# =========================

numeric_only_cols = Basket.select_dtypes(include='number')
print("Correlation Matrix:\n", numeric_only_cols.corr())

# =========================
# Recommendation Tables
# =========================

df_metrics = Basket[['Team','Age','WinRate','ChampRate']]

# Top 10 by WinRate
table1 = df_metrics.sort_values(by='WinRate', ascending=False).head(10)
# Top 10 by ChampRate
table2 = df_metrics.sort_values(by='ChampRate', ascending=False).head(10)

print("Top 10 Teams by WinRate:\n", table1)
print("Top 10 Teams by ChampRate:\n", table2)


# =========================
# PART 3 - STARTUP DATA
# =========================

data = pd.read_csv("CompanyX_EU.csv")

df1 = data.dropna().copy()

df1['Funds_in_million'] = df1['Funding'].apply(
    lambda x: float(x[1:-1])/1000 if x[-1]=='K' else
              (float(x[1:-1])*1000 if x[-1]=='B' else float(x[1:-1]))
)

# Boxplot
plt.boxplot(df1.Funds_in_million)
plt.show()

# Remove outliers
upper_fence = plot['caps'][1].get_data()[1][1]

df1 = df1[df1.Funds_in_million <= upper_fence]

# Hypothesis Testing
from statsmodels.stats.weightstats import ztest
from scipy.stats import ttest_ind

sample1 = df1[df1.OperatingState == 'Operating']['Funds_in_million']
sample2 = df1[df1.OperatingState == 'Closed']['Funds_in_million']

alpha = 0.05

z_stat, p_val = ztest(sample1, sample2)
print("Z-test p-value:", p_val)

t_stat, p_val = ttest_ind(sample1, sample2)
print("T-test p-value:", p_val)

# Proportion Test
from statsmodels.stats.proportion import proportions_ztest

df2 = data.copy()

winners = df2[df2.Result != 'Contestant']
contestants = df2[df2.Result == 'Contestant']

winners_operating = winners[winners.OperatingState=='Operating'].shape[0]
contestants_operating = contestants[contestants.OperatingState=='Operating'].shape[0]

count = [contestants_operating, winners_operating]
nobs = [len(contestants), len(winners)]

stat, pval = proportions_ztest(count, nobs)

print("Proportion test p-value:", pval)