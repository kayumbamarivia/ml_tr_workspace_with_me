import pandas as pd
data = {"color":['red', 'blue', 'green', 'red', 'green','green']}
df = pd.DataFrame(data)

freq = df["color"].value_counts(normalize=True)
print(freq)