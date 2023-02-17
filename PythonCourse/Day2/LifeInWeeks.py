age = input("What is your current age? ")

remainingYearsofAge = 90 - int(age)

days = remainingYearsofAge * 365
weeks = remainingYearsofAge * 52
months = remainingYearsofAge * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")