import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
data = pd.read_csv("F:\Study mterials\Machine learning\ML1RSMBADS1.csv",header = None)
data = data.head(50)
data.fillna('na',inplace=True)
data = data.values
data = data.tolist()
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)
df.drop('na',axis=1,inplace=True)
#print(df)
import pyfpgrowth

patterns=pyfpgrowth.find_frequent_patterns(df,50)
rules=pyfpgrowth.generate_association_rules(patterns, .7)
print(rules)
