####### Data types ###########
'''
there are 5 main data types are there in Python
1. numbers
2. strings
3. lists
4. tupuls
5. dictionaries or map

'''

# integer
age = 20
print(age)

# reassigning the value
age = 30
print(age)

# float
price = 19.34
print(price)

# string
first_name = "Shreyata"
print(first_name)

# boolean
is_online = False
print(is_online)

####### Type conversion ##########
birth_year = input("Enter your birth year: ")
age = 2021 - int(birth_year)
print(age)

# Calculator example for data type conversion
first = input("First number - ")
second = input("Second number - ")
sum = float(first) + float(second)
print("Sum - " + str(sum))

### Strings ######
course = "Python for beginners"
print(course)
print(course.upper())
print(course.lower())
print(course.capitalize())
print(course.find('P'))
print(course.find('p')) # python is case sensitive, hence it will return -1
print(course.find('for'))
print(course.replace('for', '4'))
print('Python' in course) # another way to find string
print(course[0:6])       # print 0 to 6 char
print(course[-5:])        # print last 5 char
print(course[:-5])        # prints upto the last 5 char
print(course[:6] + " is dangerous animal")
print(course.strip())    # to strip white spaces in the end
word_list = course.split(" ")
print(word_list)

print("%c is my %s letter and number %d number is %.5f" % ('X', 'favorite', 1, .14))

########### Lists ##############
grocery_list = ['Nuts', 'Juice', 'milk', 'tomato', 'bananas']
print(grocery_list)
print("First item is ", grocery_list[0])
print("Last item is ", grocery_list[-1])
grocery_list[2] = "Yogurt"   # replaced milk with yogurt
print("Replaced item is ", grocery_list[2])
print(grocery_list[0:3])
print("The final list is now: ", grocery_list)

# nested list
tasks_list = ['wash car', 'write assignment', 'submit proposal']
to_do_list = [tasks_list, grocery_list]
print(to_do_list)
print(to_do_list[1][2])

### List methods
print("Grocery list after sorting: ", grocery_list.sort())
print("Grocery list after reverse sorting: ", grocery_list.reverse())

numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.append(6)
print(numbers)
numbers.insert(0, -1)
print(numbers)
numbers.remove(3)
print(numbers)
# numbers.clear()
# print(numbers)
del numbers[3]
print(1 in numbers)  # to check if 1 exists in the list 'number'. It returns a boolean value
print(len(numbers))  # to get the number of items in the list or length of the list

combined_list = to_do_list + numbers
print("The combined list is: ", combined_list)
print(len(combined_list))

combined_list_2 = grocery_list + tasks_list + numbers
print("The combined list 2 is:", combined_list_2)
print(len(combined_list_2))
print(min(numbers))
print(max(numbers))



# ########### Tuples #######
pi_tuple = (4,3,6,7,1)
print(pi_tuple)
new_list = list(pi_tuple)  # converting tuple into list and then list can be edited
print(new_list)
new_tuple = tuple(new_list) # converting back list to tuple
print(new_tuple)
print("Lenth of the tuple is: ", len(new_tuple))
print("Min in the tuple is: ",min(new_tuple))
print("Max in the tuple is: ", max(new_tuple))


############ Dictionaries ################
super_villains = {'Fiddler': 'Isaac Bowin',
                  'Captain Cold': 'Leonard Snart',
                  'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder',
                  'Pide Piper': 'Thomas Peterson'}
print(super_villains['Captain Cold'])
del super_villains['Fiddler']
super_villains['Pide Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get("Pide Piper"))
print(super_villains.keys())
print(super_villains.values())