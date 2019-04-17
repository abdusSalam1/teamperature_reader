class YearlyTemperatureReport:
    year = ""
    min_temperature = max_temperature = 0.0

    def __init__(self):
        pass

    def merge(self, raw_temperature):
        raw_temperature_entries = raw_temperature.split(',')
        self.merge_max_temperature(self.get_float_value(raw_temperature_entries[1]))
        self.merge_min_temperature(self.get_float_value(raw_temperature_entries[3]))
        self.year = raw_temperature_entries[0].split('-')[0]

    def merge_max_temperature(self, max_temperature):
        if max_temperature != "" and max_temperature > self.max_temperature:
            self.max_temperature = max_temperature

    def merge_min_temperature(self, min_temperature):
        if min_temperature != "" and min_temperature > self.min_temperature:
            self.min_temperature = min_temperature

    def get_float_value(self, value):
        return float(value) if not value == '' else 0.0
