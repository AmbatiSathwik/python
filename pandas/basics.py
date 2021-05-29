import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,np.nan,6,7])
#print(s)

date = pd.date_range('20210528',periods=10,freq='5D') #5days '5H' for 5 hours
#print(date)


df = pd.DataFrame(np.random.randn(10,3),index = date,columns=['Mrng','Afnoon','night'])
#print(df)

df.apply(np.cumprod)
#print(df)
#print(df.apply(lambda x: x.max()-x.min()))

#print(s.value_counts())

s = pd.Series(['sathwik','python','vsc',np.nan,'list','recommend'])
#print(s.str.upper())

df2 = pd.DataFrame(np.random.randn(10,4))
#print(df2)
#df2 = [df2[:3], df2[3:7], df2[7:]]
#print(df2)
#print(pd.concat(df2))


left = pd.DataFrame({'A': [1,2], 'B': [3,4]})
right = pd.DataFrame({'A': [3,1], 'C': [4,5]})
#print(left)
#print(right)
#print(pd.merge(left,right,on='A'))
#
#print(df2.groupby([0,1]).sum())


my_tupple = list(zip(*[[1,2,3,4,5,17,18,19], [11,12,13,6,7,8,9,10]])) # * is used for mapping 1 with 11 and 2 with 12 so on
print(my_tupple)
index = pd.MultiIndex.from_tuples(my_tupple, names = ['First','second'])
print(index)
df3 = pd.DataFrame(np.random.randn(8,2),index = index, columns=['A','B'])
print(df3.stack())

