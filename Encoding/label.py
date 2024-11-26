from sklearn.preprocessing import LabelEncoder
import pandas as pd
# Using pandas
data_pd = {"color":['red', 'blue', 'green', 'red', 'green']}
df = pd.DataFrame(data_pd)
mapping = {"red": 2, "blue": 0, "green" : 1}

df["labeled_data"] = df["color"].map(mapping)
df=df.drop('color',axis=1)
print(df)
# Using Sklearn
print("\n")
data = ['red', 'blue', 'green', 'red', 'green']
le = LabelEncoder()
labeled_data = le.fit_transform(data) 
print(labeled_data)