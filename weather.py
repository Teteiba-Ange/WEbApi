from pyowm.owm import OWM

location = input("PLease enter yor location :")
API_KEY="f9da3e8cca6bf4066ae78b6aabd7f513"
owm = OWM(API_KEY)
weather_manager = owm.weather_manager()

observation = weather_manager.weather_at_place(location)
w = observation.weather

weatherWind=w.wind()
weatherHumidity=w.humidity
weatherTemperature= w.temperature('celsius')
weatherStatus= w.detailed_status

forecast = f"The weather at {location} is {weatherStatus} with a Tempearture of {weatherTemperature['temp']}  and {weatherWind['speed']} and a humidity of {weatherHumidity}"
if weatherTemperature <= 30:
    print(forecast)
else:
    print("The weather at the specified location must be  more than 30")
