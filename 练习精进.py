
import pandas as pd
df = pd.DataFrame(data={'height':[178,171,185,196],'weight':[156,90,140,142],
						'name':['小王','小明','小绿','小红']})
print(df)
df1=df.set_index('name',drop=False)
print(df1)
df2=df.set_index('name',drop=True) #是否删除作为索引使用的列，默认True,即删除做为索引的列
print(df2)
