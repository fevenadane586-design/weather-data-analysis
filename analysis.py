import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('weather_data.csv')

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Calculations
avg_temp = df['Temperature'].mean()
hottest_day = df.loc[df['Temperature'].idxmax()]
coldest_day = df.loc[df['Temperature'].idxmin()]

# Print results
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Hottest Day: {hottest_day['Date'].date()} ({hottest_day['Temperature']}°C)")
print(f"Coldest Day: {coldest_day['Date'].date()} ({coldest_day['Temperature']}°C)")

# Plot
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Temperature'], marker='o', color='orange')
plt.title('Daily Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_plot.png')  # Save plot
plt.show()