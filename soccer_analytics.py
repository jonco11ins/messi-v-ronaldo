import requests
import json
import os
import csv
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
MESSI_ID=154
RONALDO_ID=874
url = "https://api-football-v1.p.rapidapi.com/v3/players"
start_year= 2003
end_year= 2023

headers = {
	"X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}
for year in range(start_year, end_year):
	print(year)
	MESSI_querystring = {"id":MESSI_ID,"season":year}
	response_MESSI = requests.request("GET", url, headers=headers, params=MESSI_querystring)
	print(response_MESSI.text)

	if(len(response_MESSI.json()["response"]) > 0):
		rmj=response_MESSI.json()["response"][0]["statistics"]
		dfm = pd.read_json(json.dumps(rmj))
		dfm.to_csv(f"messi_data_{year}.csv", mode="w",encoding='utf-8', index=False)

	RONALDO_querystring = {"id":RONALDO_ID,"season":year}
	response_RONALDO = requests.request("GET", url, headers=headers, params=RONALDO_querystring)
	print(response_RONALDO.text)
	if(len(response_RONALDO.json()["response"]) > 0 ):
		rrj=response_RONALDO.json()["response"][0]["statistics"]
		dfr = pd.read_json(json.dumps(rrj))
		dfr.to_csv(f"ronaldo_data_{year}.csv", mode="w",encoding='utf-8', index=False)

	

