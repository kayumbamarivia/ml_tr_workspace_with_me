import pandas as pd

data = {
    "color":["red", "green", "blue"],
    "gender":["female","male", "none"]
}

df = pd.DataFrame(data)
# The data arrays should have the same length
one_hot_df = pd.get_dummies(df, columns=["color", "gender"])
one_hot_df = one_hot_df.astype(int)
print(one_hot_df.to_string(index=False))