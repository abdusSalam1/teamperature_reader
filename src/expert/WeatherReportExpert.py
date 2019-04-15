from expert import WeatherFileExpert


class WeatherFileExpert:
    DIRECTORY_PATH = "data/weatherdata"
    weatherFileExpert = {}

    def __init__(self):
        self.weatherFileExpert = WeatherFileExpert()

    def create_weather_report(self):
        yearly_weather_reports = self.weatherFileExpert.read_yearly_weather(self.DIRECTORY_PATH)