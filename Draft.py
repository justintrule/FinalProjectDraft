import requests, json

apiKey = "6c1d46d4aa29137a45b613d3111afacb"

print("Connecting to api....")
print("")
print("Connected!")
print("")

cityName = input("Enter city or zipcode for up to date weather: ")

url = "http://api.openweathermap.org/data/2.5/weather?"

completeURL = url + "appid=" + apiKey + "&q=" + cityName + "&units=imperial"

response = requests.get(completeURL)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    cityTemp = y["temp"]
    cityHumid = y["humidity"]
    z = x["weather"]
    weatherDescription = z[0]["description"] 
    print(" The current weather conditions in", cityName, "are",  "Temperature = " + str(cityTemp) + "\n Humidity Percentage = " + str(cityHumid)+"\n Conditions = " + str(weatherDescription)) 
  
else: 
    print(" City Not Found : Press 'enter' to restart program ")
