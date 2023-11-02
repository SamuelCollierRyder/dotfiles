import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gdp_per_capita = pd.read_csv("gdp-per-capita-penn-world-table.csv")
life_expectancy = pd.read_csv("life-expectancy.csv")
gdp = pd.read_csv("national-gdp-penn-world-table.csv")

life_expectancy_2019 = life_expectancy.loc[life_expectancy['Year'] == 2019]
gdp_per_capita_2019 = gdp_per_capita.loc[gdp_per_capita['Year'] == 2019]
gdp_2019 = gdp.loc[gdp['Year'] == 2019]

avg_life_exp_2019 = life_expectancy_2019['Period life expectancy at birth - Sex: all - Age: 0'].mean()
std_life_exp_2019 = life_expectancy_2019['Period life expectancy at birth - Sex: all - Age: 0'].std()
avg_gdp_2019 = gdp_2019['GDP (output, multiple price benchmarks)'].mean()

combined_df = life_expectancy_2019.merge(gdp_2019, 'inner', on=['Code', 'Entity', 'Year'])
combined_df_capita = life_expectancy_2019.merge(gdp_per_capita_2019, 'inner', on=['Code', 'Entity', 'Year'])

# print(combined_df)

# 1. 
# print(life_expectancy_2019.loc[life_expectancy_2019['Period life expectancy at birth - Sex: all - Age: 0'] > avg_life_exp_2019+std_life_exp_2019])

# 2. 
x = combined_df.loc[(combined_df['GDP (output, multiple price benchmarks)'] < avg_gdp_2019) & (combined_df['Period life expectancy at birth - Sex: all - Age: 0'] > avg_life_exp_2019)]
print(x)



# plt.boxplot(life_expectancy_2019['Period life expectancy at birth - Sex: all - Age: 0'])
# plt.scatter(combined_df['Period life expectancy at birth - Sex: all - Age: 0'], combined_df['GDP per capita (output, multiple price benchmarks)'])
# plt.title('GDP per capita in relation to life expectancy')
# plt.xlabel('Life Expectancy')
# plt.ylabel('GDP per capita')
# plt.show()