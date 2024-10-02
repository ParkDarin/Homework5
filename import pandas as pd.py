import pandas as pd

fish_df = pd.read_csv('/Users/Darin/Downloads/capture-fishery-production.csv')
population_df = pd.read_csv('/Users/Darin/Downloads/population.csv')

fish_df = fish_df[fish_df['Year'] == 2020]
population_df = population_df[population_df['Year'] == 2020]
population_df = population_df.rename(columns={'Population - Sex: all - Age: all - Variant: estimates': 'Population_2020'})


filtered_df = pd.merge(fish_df, population_df, left_on='Entity', right_on='Entity', how='inner')

filtered_df['Entity'] = filtered_df['Entity'].replace('United States', 'United States of America')
filtered_df['Entity'] = filtered_df['Entity'].replace('Democratic Republic of Congo', 'Dem. Rep. Congo')
filtered_df['Entity'] = filtered_df['Entity'].replace('Central African Republic', 'Central African Rep.')
filtered_df['Entity'] = filtered_df['Entity'].replace('Cote d\'Ivoire', 'Côte d\'Ivoire')
filtered_df['Entity'] = filtered_df['Entity'].replace('Solomon Islands', 'Solomon Is.')
filtered_df['Entity'] = filtered_df['Entity'].replace('Eswatini', 'eSwatini')
filtered_df['Entity'] = filtered_df['Entity'].replace('South Sudan', 'S. Sudan')
filtered_df['Entity'] = filtered_df['Entity'].replace('Bosnia and Herzegovina', 'Bosnia and Herz.')	

filtered_df = filtered_df.drop(columns=['Code_y', 'Year_x', 'Year_y'])

print(filtered_df.head())

output_path = '/Users/Darin/Downloads/capture-fishery-production-2020.csv'
filtered_df.to_csv(output_path, index=False)