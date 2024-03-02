# %% 
import pandas as pd
import json
# %%

df = pd.read_json("twitter-450mb.json")

# %%
df = pd.read_json("twitter-50mb.json")

# %%
d = json.load(open('twitter-450mb.json', encoding="utf-8"))
df = pd.DataFrame.from_dict(d, orient="index")
# %%
df["value"]
# %%
for col in df.columns:
    print(col)
# %%
df["rows"][0]["data"]
