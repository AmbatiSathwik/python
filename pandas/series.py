import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4,np.nan,5,6])
#print(s)

date = pd.date_range('20210528',periods=30,freq='5D') #5days '5H' for 5 hours
#print(date)

df = pd.DataFrame(np.random.randn(30,3),index = date,columns=['Mrng','Afnoon','night'])
print(df)
