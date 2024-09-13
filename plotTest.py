import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import numpy as np
import database as db

import csv

leftovers2018 = db.load("fixed-leftovers/2018LeftoversFixed")
leftovers2019 = db.load("fixed-leftovers/2019LeftoversFixed")
leftovers2020 = db.load("fixed-leftovers/2020LeftoversFixed")
leftovers2021 = db.load("fixed-leftovers/2021LeftoversFixed")
leftovers2022 = db.load("fixed-leftovers/2022LeftoversFixed")
leftovers2023 = db.load("fixed-leftovers/2023LeftoversFixed")

valences2018 = db.load("fixed-valences/2018ValencesFixed")
valences2019 = db.load("fixed-valences/2019ValencesFixed")
valences2020 = db.load("fixed-valences/2020ValencesFixed")
valences2021 = db.load("fixed-valences/2021ValencesFixed")
valences2022 = db.load("fixed-valences/2022ValencesFixed")
valences2023 = db.load("fixed-valences/2023ValencesFixed")

allLeftovers = leftovers2018 + leftovers2019 + leftovers2020 + leftovers2021 + leftovers2022 + leftovers2023

for x in allLeftovers:
    if (len(x[1]) != 0):
        print(len(x[1]))

data = valences2018 + valences2019 + valences2020 + valences2021 + valences2022 + valences2023
valences = [sublist[1] for sublist in data]
dates = [sublist[0] for sublist in data]



rolling = []
window = 10
rollingDates = dates[window: len(data) - window]
for i in range(window, len(data) - window):
    rolling.append(np.mean(valences[i - window: i + window]))

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=365))
plt.axvline(x = datetime.datetime(2020, 3, 11), color = "r")

plt.gcf().autofmt_xdate()
plt.plot(dates, valences)
plt.show()

'''
plt.axvspan(datetime.datetime(2018, 11, 1), datetime.datetime(2019, 1, 15), color = "r", alpha = .5)
plt.axvspan(datetime.datetime(2019, 11, 1), datetime.datetime(2020, 1, 15), color = "r", alpha = .5)
plt.axvspan(datetime.datetime(2020, 11, 1), datetime.datetime(2021, 1, 15), color = "r", alpha = .5)
plt.axvspan(datetime.datetime(2021, 11, 1), datetime.datetime(2022, 1, 15), color = "r", alpha = .5)
plt.axvspan(datetime.datetime(2022, 11, 1), datetime.datetime(2023, 1, 15), color = "r", alpha = .5)
plt.axvspan(datetime.datetime(2023, 11, 1), datetime.datetime(2024, 1, 15), color = "r", alpha = .5)






with open(r"/Users/aaronyang/Desktop/School/Research/spotify-research/valences.csv", "w") as f:
    writer=csv.writer(f)
    writer.writerow(["Dates", "Data"])
    for i in data:
        writer.writerow([i[0].strftime("%Y-%m-%d"),i[1]])
        '''