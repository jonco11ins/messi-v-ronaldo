import requests
import os
from dotenv import load_dotenv
load_dotenv()
url = "https://api-football-v1.p.rapidapi.com/v3/players"

querystring = {"search":"ronaldo"}

headers = {
	"X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.json())

# id:33
# name:"Manchester United"
#id:874
#name:"Cristiano Ronaldo"

# id:85
# name:"Paris Saint Germain"\
# id:154
# name:"L. Messi"