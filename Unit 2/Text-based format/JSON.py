import json
import pandas as pd

json_data = open('LondonWeather.json').read()
data = json.loads(json_data)

weather_data = pd.DataFrame(data["main"],
                            index=[data["name"]])

pd.io.json.json_normalize(data['main'])


