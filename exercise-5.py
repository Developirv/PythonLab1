# DELIVERABLE LAB 03/05/2019 5/6

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:

# 1. Calculates and prints the first 50 terms of the fibonacci sequence.

f = 1
current = 1
former = 0

for term in range (50):
  if term == 0:
    print(f"term: {term} / number: 0")
  elif term == 1:
    print(f"term: {term} / number: 1")
  else:
    f = current + former
    print(f"term: {term} / number: {f}")
    former = current
    current = f

# 2. Print each term and number as follows:

# ^^