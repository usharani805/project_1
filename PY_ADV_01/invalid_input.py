try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age")
    else:
        print("Your age is:", age)

except ValueError:
    print("Invalid input. Please enter a number.")