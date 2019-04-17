from expert import WeatherFileExpert


class WeatherReportExpert:
    DIRECTORY_PATH = "data"
    weatherFileExpert = {}

    def create_weather_report(self):
        print("Reading reports")
        yearly_weather_reports = WeatherFileExpert.WeatherFileExert().read_yearly_weather(self.DIRECTORY_PATH)
        print("Done reading reports")
        return yearly_weather_reports
