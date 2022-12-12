
import csv
import json
import pandas as pd

sample_api_response = {"data": {"data": "hello!"}}
 # 1. append to data.csv
print(sample_api_response)
# Write the data to a CSV file
df = pd.read_json(json.dumps(sample_api_response))
df.to_csv("data.csv", mode="a",encoding='utf-8', index=False)
