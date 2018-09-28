# duplicates in dataframe
import pandas as pd
df = pd.DataFrame({'A':['foo','foo', 'foo', 'bar'], 'B': [0,1,1,1], 'C':['A','A','B','A']})
df.drop_duplicates(subset=['A','C'], keep=False)

# duplicates in a list
def remove(duplicates):
    final_list = []
     for num in duplicates:
       if num not in final_list:
            final_list.append(num)
     return final_list
duplicates = [2,2,44,5,33,33,8,4,5]
print(remove(duplicates))