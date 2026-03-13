import requests

url = "https://azone-real-time-amazon-data-api.p.rapidapi.com/product-details"

querystring = {
    "asin": "B0B8G1Q9DM",
    "country": "US"
}

headers = {
    "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
    "X-RapidAPI-Host": "azone-real-time-amazon-data-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
