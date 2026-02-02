import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=29.02&longitude=-81.30&current_weather=true"
resp = requests.get(url).json()
celc_temp = resp["current_weather"]["temperature"]
print("The currrent temperature in DeLand, Florida is: ", (celc_temp * 9/5) + 32)