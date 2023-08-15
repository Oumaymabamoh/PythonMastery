print("Hello World ")
print("*" * 10)

course = "Python Programming"
print(len(course))
# slice a string
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

# escape sequences \" \' \\ \n
course_name = "Python course"

# formmated strings
first = "hello"
last =  "all"
full = f"{first} {last}"
full = f"{len(first)} {last}"
print(full)

# string methods
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.rstrip())
print(course.find("Pro"))
print(course.replace("P", "J"))
print("Prp" in course)
print("swift" not in course)

# numbers
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

#working with numbers

import math
print(round(2.9))
print(abs(-2.9))

print(math.ceil(2.2))

# type conversion
x = input ("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")

#conditional statements
temperature = 15
if temperature > 30:
    print("It's warm ")
    print("Drink water")
elif temperature > 20:
    print("It's nice ")
else:
    print("It's cold")
print("Done")

#ternary oparator
age = 22
message = "Eligible" if age >= 18 else "Not elegible"
print(message)

#logical operators
high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not elegible")

# age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")

# loops
for number in range(1,4):
  print("Attempt", number, number  * ".")

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

# while loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command != "quit":
     command = input(">")
     print("WCHO", command)
#
count = 0
for number in range(1,10):
    if number % 2 == 0:
       count += 1
       print(number)
print(f"we have {count} even number")


