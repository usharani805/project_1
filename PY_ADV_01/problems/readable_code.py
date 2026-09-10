# Refactored code for better readability

def check_age(age):
    if age == 0:
        return "Age cannot be zero."

    if age > 120:
        return "Age is too high."

    return f"Valid age: {age}"


age = int(input("Enter your age: "))

result = check_age(age)

print(result)