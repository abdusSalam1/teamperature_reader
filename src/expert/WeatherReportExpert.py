from expert import WeatherFileExpert


class WeatherFileExpert:
    DIRECTORY_PATH = "data/weatherdata"
    weatherFileExpert = {}

    def __init__(self):
        self.weatherFileExpert = WeatherFileExpert()

    def create_weather_report(self):
        # Here we have got the yearly report with min and max temperature in a year
        yearly_weather_reports = self.weatherFileExpert.read_yearly_weather(self.DIRECTORY_PATH)