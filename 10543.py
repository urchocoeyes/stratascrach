# Second Highest Salary

import pandas as pd

employee_data = employee_data.sort_values(by=['department', 'salary'],
                                          ascending=['True', 'False'])

# actually we can just write rank
second_highest_salary = employee_data[employee_data['rank'] == 2]

final_result = second_highest_salary[['department', 'employee_id', 'salary']]

final_result