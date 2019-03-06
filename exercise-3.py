# DELIVERABLE LAB 03/05/2019 3/6

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dog_age = int(input("Input Lila's age in human years: "))

if dog_age == 1 or dog_age == 2:
  dog_age *= 10
  print(f"Lila's age in dog years is {dog_age}")
else:
  age = 0
  for year in range(1, dog_age + 1):
    if year == 1 or year == 2:
      age += 10
    else:
      age += 7
  print(f"Lila's age in dog years is {age}")
