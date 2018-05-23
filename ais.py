import time
print("Hello and welcome to my 'age in seconds' calculator! Please press enter to continue.")
time.sleep(2)
user_years = input("Press Enter Now")

# user_info_asked
user_years = input("Total Years : ")
user_days = input("Total Extra Days : ")
user_hours = input("Total Extra Hours : ")
user_minutes = input("Total Extra Minutes : ")
# some_so-called_humorus_statements
print("Please wait for few secs while I calculate your age!")
time.sleep(2)
print("This will take time.")
time.sleep(2)
print("Damn! Some more time.")
time.sleep(2)
print("Unfortunately I'm not fast :(")
time.sleep(2)
print("Almost there?")
time.sleep(4)
print("Nah. Don't think so.")
time.sleep(2)
print("Hurray, I'm done here.")
time.sleep(2)
print("Pretty impressive, hun? What do you eat?")
time.sleep(3)

# integer_conversion_of_data
int(user_years)
int(user_days)
int(user_hours)
int(user_minutes)

# conversion_in_seconds
years_in_seconds = int(user_years) * 365.25 * 24 * 60 * 60
days_in_seconds = int(user_days) * 24 * 60 * 60
hours_in_seconds = int(user_hours) * 60 * 60
minutes_in_seconds = int(user_minutes) * 60

# total_age
total_seconds = years_in_seconds + days_in_seconds + hours_in_seconds + minutes_in_seconds
print('\n')
print('\n')
print("You")
time.sleep(1)
print("have")
time.sleep(1)
print("successfully")
time.sleep(1)
print("lived")
time.sleep(1)
print("{} plus few more seconds you wasted calculating. Hehe.".format(total_seconds))
time.sleep(5)
print('\n')
print('\n')
print("An idiotic bot at its best! Hun???")
time.sleep(3)
print('\n')
print('\n')
print("Credits: VikasRana")