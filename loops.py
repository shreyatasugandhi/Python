######### While loop #####
print("Simple while loop")
i = 1
while i<= 10:
    print(i * '*')
    i = i +1

# while loop with list
print("While loop with list")
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# while loop with control flow and conditions
print("While loop with control flow and conditions")
i = 0

while(i <= 20):
    if(i%2 == 0):      # if number is even number
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1


######## For loop #########
print("Simple for loop")
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

# Range function
print("Range in for loop")
numbers = range (5)
print(numbers)
for num in numbers:
    print(num)

# Range function with a step in range
print("for loop - Range function with a step in range")
num_range = range(5, 15, 2)
for num in num_range:
    print(num)

# OR

for num in range(5, 15, 2):
    print(num)

##### Nested for loop #######
print("Nested for loop")
num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])
