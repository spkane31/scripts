import datetime, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-miles", help="Switch to miles as the base unit", dest='miles', type=bool, default=True)
parser.add_argument("-longrun", help="Long run already completed", dest='long_run', type=bool, default=False)

args = parser.parse_args()

today = datetime.datetime.today()
weekly_mileage = float(input("Goal Weekly Mileage: "))

weekly_mileage = weekly_mileage * 1.609344

print(f"In Kilometers: {round(weekly_mileage, 1)}.\n")

long_run = round(weekly_mileage * .20, 2)
daily = round((.80 * weekly_mileage) / 6.0, 2)

print(f"Long Run: {round(long_run, 1)}")
print(f"Daily Run: {round(daily, 1)}")
to_date = float(input("Mileage Thus Far: ")) * 1.609344

remaining = weekly_mileage - to_date
print(f"In Kilometers: {round(remaining, 2)}.\n")
day_of_week = today.weekday()

if args.long_run:
  daily = remaining / (6 - day_of_week)
  daily = round(daily, 2)

  print(f"Daily Mileage Needed: {daily}" )

else:
  remaining -= long_run
  daily = remaining / (6 - day_of_week - 1)
  print(f"Long Run of {long_run} kms.")
  print(f"Daily Runs of {round(daily, 2)} kms.")