# Solutions to Python Practice Questions: Comments, Escape Sequences, and Print Statements

# Comments

# 1. Single-line Comments
# This line of code assigns the value 10 to the variable x
x = 10

# 2. Multi-line Comments
"""
This block of code initializes a variable y with the value 20,
adds the values of x and y, and stores the result in the variable z.
Finally, it prints the value of z.
"""
y = 20
z = x + y
print(z)

# 3. Docstrings
def add(a, b):
    """
    This function takes two parameters a and b,
    and returns their sum.
    """
    return a + b

# Escape Sequences

# 4. Newline Character
print("Hello, World!\nWelcome to Python programming.")

# 5. Tab Character
print("Item 1\tItem 2\tItem 3")

# 6. Backslash Character
print("C:\\new_folder\\test.txt")

# 7. Single and Double Quotes
print('She said, "Python\'s syntax is easy to learn."')

# 8. Escape Sequence Challenge
print("Name: John Doe\nAge: 30\nAddress: 123 Main St, Apt #5")

# Print Statements

# 9. Basic Print Statement
print("Hello, Python!")

# 10. Print with Variables
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# 11. String Concatenation
str1 = "Python "
str2 = "is "
str3 = "awesome!"
print(str1 + str2 + str3)

# 12. Formatted Strings
pi_value = 3.14
print(f"The value of pi is approximately {pi_value}")

# 13. Old-style String Formatting
print("The value of pi is approximately %.2f" % 3.14)

# 14. Print with Separator and End
print("Hello", "World", sep=", ", end="")

# 15. Advanced Print Formatting
print("\n| Name   | Age | Country   |")
print("|--------|-----|-----------|")
print("| Alice  | 30  | USA       |")
print("| Bob    | 25  | Canada    |")
print("| Charlie| 35  | UK        |")
