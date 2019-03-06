# DELIVERABLE LAB 03/05/2019 6/6

# exercise-06 What's the Season?

# Write the code that:


# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):

month = input('Enter a month in the year: ').lower()


# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:

day = int(input('Enter a day of the month: '))

months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall

winter = ["dec", "jan", "feb", "mar"]
spring = ["mar", "apr", "may", "jun"]
summer = ["jun", "jul", "aug", "sep"]
fall = ["sep", "oct", "nov", "dec"]

if month not in months:
  print("That's not a month")

# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# winter 
if month in winter:
  if (month == "dec" and day >= 21) or (month == "mar" and day <= 19):
    print(f"{month} {day} is in winter")
  elif month == "jan" or month == "feb":
    print(f"{month} {day} is in winter")
# spring 
if month in spring:
  if (month == "mar" and day >= 20) or (month == "jun" and day <= 20):
    print(f"{month} {day} is in spring")
  elif month == "apr" or month == "may":
    print(f"{month} {day} is in spring")
# summer 
if month in summer:
  if (month == "jun" and day >= 21) or (month == "sep" and day <= 21):
    print(f"{month} {day} is in summer")
  elif month == "jul" or month == "aug":
    print(f"{month} {day} is in summer")
# fall 
if month in fall:
  if (month == "sep" and day >= 22) or (month == "dec" and day <= 20):
    print(f"{month} {day} is in fall")
  elif month == "oct" or month == "nov":
    print(f"{month} {day} is in fall")

# End