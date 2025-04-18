# Function to convert Roman to Integer
def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

# Function to convert Integer to Roman
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90,  50, 40,
        10,  9,   5,  4, 1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    roman = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman += syms[i]
            num -= val[i]
        i += 1
    return roman

# Input from user
n1 = input("Enter the first Roman numeral: ").upper()
n2 = input("Enter the second Roman numeral: ").upper()

# Convert to integers
int1 = roman_to_int(n1)
int2 = roman_to_int(n2)

# Sum
total = int1 + int2

# Check if within limit
if total >= 4000:
    print("The result exceeds typical Roman numeral range (less than 4000).")
else:
    roman_result = int_to_roman(total)
    print(f"Integer sum: {total}")
    print(f"Roman numeral sum: {roman_result}")






