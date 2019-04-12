import glob
import logging
import os

from domain.YearlyTemperatureReport import YearlyTemperatureReport


class WeatherFileExert:

    FILE_EXTENSION = "*.txt"

    def __init__(self):
        pass

    def read_yearly_weather(self, directory_path):
        try:
            readable_files = glob.glob(os.path.join(directory_path, self.FILE_EXTENSION))
            for file in readable_files:
                daily_temperatures = open(file, 'r').readlines()
                self.get_yearly_temperature_report(daily_temperatures)
        except:
            logging.error('Error while reading file')

    def get_yearly_temperature_report(self, daily_temperatures):
        yearly_temperature_report = YearlyTemperatureReport()
        for raw_temperature in daily_temperatures:
            if self.is_valid_temperature(raw_temperature):
                yearly_temperature_report.merge(raw_temperature)
        return yearly_temperature_report

    def is_valid_temperature(self, data):
        return data.strip() and not data.startswith("<!--")
