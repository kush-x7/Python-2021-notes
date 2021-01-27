my_age = int(input("enter you current age: "))

years_remaining = 90 - my_age
days_remaining = years_remaining *365
weeks_remaining = years_remaining *52
months_remaining = years_remaining*12

print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left.")
