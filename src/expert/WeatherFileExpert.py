import glob
import os


class WeatherFileExert:

    def __init__(self):
        pass

    def read_weather(self, directory_path):
        readable_files = glob.glob(os.path.join(directory_path, "*.txt"))
        for file in readable_files:
            raw_data = open(file, 'r').readlines()
        for data in raw_data:
            if data.strip() and not data.startswith("<!--"):
                pass