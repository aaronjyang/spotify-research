import csv
import database as db
#print(dir(csv))
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

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

date = datetime.datetime(2023, 1, 2)
print(date.strftime("%Y-%m-%d"))