from datetime import date

def calculate_days_lived(birth_date):
    today = date.today()
    days_lived = (today - birth_date).days
    return days_lived

# Get birth date from user
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

birth_date = date(year, month, day)

days_lived = calculate_days_lived(birth_date)
print("You have lived for", days_lived, "days.")