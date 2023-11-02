import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gdp_per_capita = pd.read_csv("gdp-per-capita-penn-world-table.csv")
life_expectancy = pd.read_csv("life-expectancy.csv")

life_expectancy_2019 = life_expectancy.loc[life_expectancy['Year'] == 2019]
gdp_per_capita_2019 = gdp_per_capita.loc[gdp_per_capita['Year'] == 2019]

print(life_expectancy_2019.mean)
# 1. 


combined_df = life_expectancy_2019.merge(gdp_per_capita_2019, 'inner', on=['Code', 'Entity', 'Year'])

# plt.boxplot(life_expectancy_2019['Period life expectancy at birth - Sex: all - Age: 0'])
# plt.scatter(combined_df['Period life expectancy at birth - Sex: all - Age: 0'], combined_df['GDP per capita (output, multiple price benchmarks)'])
# plt.title('GDP per capita in relation to life expectancy')
# plt.xlabel('Life Expectancy')
# plt.ylabel('GDP per capita')
# plt.show()