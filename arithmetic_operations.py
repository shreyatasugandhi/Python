'''
There are 7 arithmetic operators in Python
+, -, *, /, //, **, %

'''

print("10 + 3 = ", 10 + 3)
print("10 - 3 = ", 10 - 3)
print("10 * 3 = ", 10 * 3)
print("10 / 3 = ", 10 / 3)
print("10 // 3 = ", 10 // 3)  # for getting whole number/integer
print("10 % 3 = ", 10 % 3)  # modulus operator or gives the remainder
print("10 ** 3 = ", 10 ** 3)  # exponential operator

# augmented assignment operator
x = 10
x = x + 3
print(x)
# or augmented
x += 3
print(x)

# python follows the same math operator president concept in programming
x = 10 + 3 * 2
print(x)
y = (10 + 3) * 2
print(y)
