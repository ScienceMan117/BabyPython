import csv

from datetime import datetime

from matplotlib  import pyplot as plt

filename1 = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'

with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)
    
    dates1, highs1, lows1 = [], [], []
    for row in reader1:
        try:
            current_date1 = datetime.strptime(row[0], "%Y-%m-%d")
            high1 = int(row[1])        
            low1 = int(row[3])
        except ValueError:
            print(current_date1, 'missing data')
        else:
            dates1.append(current_date1)
            highs1.append(high1)
            lows1.append(low1)   
            
with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row2 = next(reader2)
    
    dates2, highs2, lows2 = [], [], []
    for row in reader2:
        try:
            current_date2 = datetime.strptime(row[0], "%Y-%m-%d")
            high2 = int(row[1])        
            low2 = int(row[3])
        except ValueError:
            print(current_date2, 'missing data')
        else:
            dates2.append(current_date2)
            highs2.append(high2)
            lows2.append(low2)   

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates1, highs1, c='red', alpha=0.5)
plt.plot(dates2, highs2, c='purple', alpha=0.5)
plt.plot(dates1, lows1, c='blue', alpha=0.5)
plt.plot(dates2, lows2, c='yellow', alpha=0.5)
plt.fill_between(dates1, highs1, lows1, facecolor='red', alpha=0.1)
plt.fill_between(dates2, highs2, lows2, facecolor='purple', alpha=0.5)

# Format plot.
title = "High and Low Temperature Comparison Between Sitka and Death Valley"
plt.title(title,  fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
