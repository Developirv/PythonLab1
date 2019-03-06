# DELIVERABLE LAB 03/05/2019 4/6

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

length_a = int(input("Enter length of side a: "))
length_b = int(input("Enter length of side b: "))
length_c = int(input("Enter length of side c: "))

if length_a == length_b and length_b == length_c:
  print(f"A triangle with sides of {length_a}, {length_b}, & {length_c} issa equalateral triangle")
elif length_a == length_b or length_b == length_c:
  print(f"A triangle with sides of {length_a}, {length_b}, & {length_c} issa isosceles triangle")
else:
  print(f"A triangle with sides of {length_a}, {length_b}, & {length_c} issa scalene triangle")