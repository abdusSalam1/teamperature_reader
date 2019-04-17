from expert import WeatherReportExpert


def main():
    report_data = WeatherReportExpert.WeatherReportExpert().create_weather_report()
    for data in report_data:
        print(data.to_string())


if __name__ == '__main__': main()
