# Weather Data Analysis 🌤️

A Python-based data analysis project that processes and visualizes weather data to identify temperature trends, calculate average temperature, and detect the hottest and coldest days — now refactored into an **object-oriented design** for better maintainability and scalability.

## 📊 Features
- Reads weather data from a CSV file
- Computes the **average temperature**
- Identifies the **hottest and coldest days**
- Generates a **line plot** showing temperature trends over time

## 🛠️ Technologies Used
- Python
- Pandas (for data processing)
- Matplotlib (for visualization)

## 📁 Project Structure (OOP Refactor)
- `main.py` – Entry point to run the analysis  
- `src/weather_analyzer.py` – Core `WeatherAnalyzer` class with modular methods

## ▶️ How to Run the Project

1. Clone this repository:  
   ```bash
   https://github.com/fevenadane586-design/weather-data-analysis.git
2.Navigate into the project folder:
   cd weather-data-analysis
3.Install required packages:
   pip install pandas matplotlib
4.Run the analysis script:
   python main.py
💡 Sample Output
When you run the code, you’ll see output like
:Loaded 365 records.
Removed 0 invalid rows.

Weather Summary:
  Average Temp: 22.94 C
  Highest Temp: 28.3 C on 2025-10-04
  Lowest Temp: 18.2 C on 2025-10-05
Plot saved to temperature_trend.png
A temperature trend plot (temperature_trend.png) will be saved in the project folder.
🌍 Built During DevTech Internship
This project was developed as part of my internship at DevTech, applying data analysis and Python programming skills to real-world datasets — with a recent refactor to demonstrate object-oriented programming best practices.

