import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, precipitation = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rainfall = float(row[19])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            precipitation.append(rainfall)
          
 
# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, precipitation, c='purple', alpha=0.5)

# Format plot.
title = "Daily Precipitation in Sitka 2014"
plt.title(title,  fontsize=20)
plt.xlabel('Date', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (In)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim([0, 1.0])

plt.show()

