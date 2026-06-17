```python
# Program 1: Largest of Three Numbers

# Method 1

a = 10
b = 20
c = 15

print("Largest number is:", max(a, b, c))


# Method 2

numbers = input("Enter exactly 3 numbers separated by spaces: ").split()

if len(numbers) != 3:
    print("Please enter exactly 3 numbers.")
else:
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number is:", largest)


# Program 2: Leap Year

# Method 1

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# Method 2

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")


# Program 3: Vowel or Consonant

# Method 1

ch = 'a'

if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")


# Method 2

ch = input("Enter a character: ")

if len(ch) != 1:
    print("Please enter only one character.")
else:
    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")


# Program 4: Check Whether a Number is Divisible by 5 and 11

# Method 1

number = 55

if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# Method 2

number = int(input("Enter a number: "))

if number % 5 == 0 and number % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# Program 5: Sum of First N Natural Numbers Using While Loop

n = int(input("Enter a number: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)


# Method 2

n = int(input("Enter a number again: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum using for loop =", total)


# Program 6: Multiplication Table

# Method 1

num = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1


# Method 2

num = int(input("Enter a number again: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# Program 7: Pyramid Pattern

rows = 4

for i in range(rows):
    spaces = rows - i - 1
    stars = 2 * i + 1

    print(" " * spaces + "*" * stars)


# Program 8: Number Pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```
