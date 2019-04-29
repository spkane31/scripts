from datetime import datetime, date

a = datetime.now()
streakStart = datetime(2018, 7, 8)
today = datetime.now()
days = (today - streakStart).days + 1

start = a.replace(month = 1, day = 1, hour = 0, minute = 0, second = 0, microsecond=0)

now = datetime.now()

dif = (now - start).days

userInput = (input("Miles to Date: "))

print(f"Consecutive days running: {days}")

milesTD = float(userInput)

dailyMileage = milesTD / dif

print("Daily Mileage: " + str(round(dailyMileage, 2)))
print("After " + str(dif) + " days you are on track for: " + str(round(dailyMileage * 365, 2)))

goalMileage = 3400

dailyMileageNeeded = (goalMileage - milesTD) / (365 - dif)
weeklyMileageNeeded = dailyMileageNeeded * 7

print("\n" + str(goalMileage) + " MILES GOAL")
print("Daily Mileage Needed: " + str(round(dailyMileageNeeded, 2)))
print("Weekly Mileage Needed: " + str(round(weeklyMileageNeeded, 2)))

previousHigh = 2628.02

dailyMileageNeeded = (previousHigh - milesTD) / (365 - dif)
weeklyMileageNeeded = dailyMileageNeeded * 7
print("\nTo have a new highest year (" + str(previousHigh) + ")")
print("Daily Mileage Needed: " + str(round(dailyMileageNeeded, 2)))
print("Weekly Mileage Needed: " + str(round(weeklyMileageNeeded, 2)))

# Monthly Mileage
start = a.replace(day = 1, hour = 0, minute = 0, second = 0, microsecond=0)
dif = (now - start).days + 1

highestMonthlyMileage = [315.01, 254.05, 293.20, 270.76, 199.27, 267.61, 283.01, 292.19, 268.01, 299.07, 229.48, 272.39]
currentMonthHigh = highestMonthlyMileage[now.month-1]
monthStr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month = now.month
if(month == 2):
  days = 28
elif(month == 4 or month == 6 or month == 9 or month == 11):
  days = 30
else:
  days = 31

userInput = input("\nMiles this month: ")
monthlyMileage = float(userInput) * days/dif
print("On Track for: " + str(round(monthlyMileage, 2)))
print(f"Average Daily: {round(monthlyMileage/30,2)}")

print(f"\nHigh for month of {monthStr[now.month-1]}: {highestMonthlyMileage[now.month-1]}")

needed = (currentMonthHigh - float(userInput)) / (days - now.day)
print(f"Daily Mileage to reach new high for month of {monthStr[now.month-1]}: {round(needed,2)}")
