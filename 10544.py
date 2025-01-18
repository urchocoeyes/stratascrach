# High density areas
# Interview Question Visa

"""
draft
df1.join(df2) - присоединяем по индексу
pd.merge(df1, df2, on='key') - осуществляю внутреннееобъединение по колонке 'key'
"""

import pandas as pd

merged_data = pd.merge(transaction_records, stores[['store_id', 
                                                   'area_name', 
                                                   'area_size']],
                                                   on='store_id')

total_number_of_uniq_customers_in_area = merged_data.groupby('area_name')['customer_id'].nunique().reset_index(name="unique_customers")

customer_density = pd.merge(total_number_of_uniq_customers_in_area, stores[['area_name', 'area_size']], 
                            on='area_name')

customer_density['density'] = customer_density['unique_customers'] / customer_density['area_size']

customer_density['rank'] = customer_density['density'].rank(method='dense', ascending=False)

top_areas = customer_density[customer_density['rank'] <= 3]

result = top_areas[['area_name', 'density']]

result