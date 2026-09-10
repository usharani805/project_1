text = "Python Programming"

vowels = "aeiou"
count = 0

for character in text.lower():
    if character in vowels:
        count += 1

print("Number of vowels:", count)