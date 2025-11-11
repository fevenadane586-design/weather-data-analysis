from src.weather_analyzer import WeatherAnalyzer

analyzer = WeatherAnalyzer("weather_data.csv")
analyzer.run_full_analysis(plot_path="temperature_trend.png")
