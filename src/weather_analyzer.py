import pandas as pd
import matplotlib.pyplot as plt
import os

class WeatherAnalyzer:
    def __init__(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Weather data file not found: {file_path}")
        self.file_path = file_path
        self.data = None

    def load_data(self, date_column: str = 'Date', temp_column: str = 'Temperature'):
        self.data = pd.read_csv(self.file_path)
        self.data[date_column] = pd.to_datetime(self.data[date_column])
        self.data.set_index(date_column, inplace=True)
        self.temp_col = temp_column
        self.date_col = date_column
        print(f"Loaded {len(self.data)} records.")
        return self.data

    def clean_data(self):
        initial = len(self.data)
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(subset=[self.temp_col], inplace=True)
        print(f"Removed {initial - len(self.data)} invalid rows.")
        return self.data

    def get_summary_stats(self):
        stats = {
            "mean_temp": round(self.data[self.temp_col].mean(), 2),
            "max_temp": self.data[self.temp_col].max(),
            "min_temp": self.data[self.temp_col].min(),
            "date_max": self.data[self.temp_col].idxmax().strftime('%Y-%m-%d'),
            "date_min": self.data[self.temp_col].idxmin().strftime('%Y-%m-%d'),
        }
        return stats

    def plot_temperature_trend(self, save_path: str = None):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data[self.temp_col], color='tab:blue')
        plt.title('Temperature Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.grid(True, linestyle='--', alpha=0.5)
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        else:
            plt.show()

    def run_full_analysis(self, plot_path: str = None):
        self.load_data()
        self.clean_data()
        stats = self.get_summary_stats()
        print("\nWeather Summary:")
        print(f"  Average Temp: {stats['mean_temp']} C")
        print(f"  Highest Temp: {stats['max_temp']} C on {stats['date_max']}")
        print(f"  Lowest Temp:  {stats['min_temp']} C on {stats['date_min']}")
        self.plot_temperature_trend(save_path=plot_path)
        return stats
