import requests

zipCode = "to be done"
countryCode = "US"
urlGeocoding = (f"http://api.openweathermap.org/geo/1.0/zip?zip={zipCode},{countryCode}&appid=d49508eda5382fe81a5b8e5b4ce7e539")

responseGeocoding = requests.get(urlGeocoding)
urlGeocoding = responseGeocoding.json()
lat = urlGeocoding['lat'] #Getting latitude from geocoding
long = urlGeocoding['lon'] #Getting longitude from geocoding