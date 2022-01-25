# Basic Version

# For the numbers 1 to 100
# Play fizzbuzz
# Print the number
# If divisible by 3, fizz
# If by 5, buzz
# if both, fizzbuzz


# What can you add?
# Can we customise the end number?
# Or the start number?
# Can we get those from player input?
# Can we input alternate words for fizz and buzz?

# Try to stick to PEP8
# Comment your code

end_num = input("Provide an end number\n")

fizz = 3
buzz = 7

for i in range(1, int(end_num) + 1):
    if i % fizz == 0 and i % buzz == 0:
        print("FizzBuzz")
    elif i % fizz == 0:
        print("Fizz")
    elif i % buzz == 0:
        print("Buzz")
    else:
        print(i)
