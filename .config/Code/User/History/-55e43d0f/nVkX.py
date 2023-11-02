import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gdp_per_capita = pd.read_csv("gdp-per-capita-penn-world-table.csv")
life_expectancy = pd.read_csv("life-expectancy.csv")

life_expectancy_2019 = life_expectancy.loc[life_expectancy['Year'] == 2019]
gdp_per_capita_2019 = gdp_per_capita.loc[gdp_per_capita['Year'] == 2019]

print(gdp_per_capita_2019)

# plt.hist(gdp_per_capita_2019['GDP per capita (output, multiple price benchmarks)'], bins=100)
plt.show()