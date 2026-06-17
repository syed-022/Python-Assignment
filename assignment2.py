
# Program 1: Area of Circle

def area_of_circle(radius):
    area = 3.14159 * radius * radius
    return area


radius = float(input("Enter radius: "))

result = area_of_circle(radius)

print("Area of Circle =", result)


# Program 2: Largest of Three Numbers

def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

result = largest(a, b, c)

print("Largest number =", result)


# Method 2

def largest_using_max(a, b, c):
    return max(a, b, c)


print("Largest number using max() =", largest_using_max(a, b, c))


# Program 3: String Length Without len()

def string_length(text):

    count = 0

    for ch in text:
        count += 1

    return count


text = input("Enter a string: ")

result = string_length(text)

print("Length =", result)


# Program 4: Prime Number Check

def is_prime(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a Prime Number")
else:
    print(number, "is not a Prime Number")


# Program 5: Fibonacci Number Using Recursion

def fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter position of Fibonacci number: "))

print("Fibonacci Number =", fibonacci(n))


# Program 6: Reverse a String Using Recursion

def reverse_string(text):

    if text == "":
        return ""

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed String =", reverse_string(text))


# Program 7: Sum of Numbers From 1 to N Using For Loop

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)


# Method 2

sum_formula = n * (n + 1) // 2

print("Sum using formula =", sum_formula)


# Program 8: Count Even Numbers in a List

numbers = [10, 15, 20, 25, 30, 35, 40]

count = 0

for num in numbers:

    if num % 2 == 0:
        count += 1

print("Even numbers count =", count)


# Method 2

count2 = sum(1 for num in numbers if num % 2 == 0)

print("Even numbers count using another method =", count2)


# Program 9: Prime Numbers Between 1 and 100

for num in range(2, 101):

    prime = True

    for i in range(2, int(num ** 0.5) + 1):

        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")
```

