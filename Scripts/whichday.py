import datetime

# Get the input for the future date
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Create a datetime object for the future date
future_date = datetime.datetime(year, month, day)

# Get the day of the week for the future date
day_of_week = future_date.strftime("%A")

# Print the day of the week
print("The day of the week for {}/{}/{} is {}".format(day, month, year, day_of_week))
