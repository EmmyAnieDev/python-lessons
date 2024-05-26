# print("Hello Python World, I am here now from Dart, hope I am welcome?")
# print('')
# name = input('tell me your name man:')
# print('My name is' + ' ' + name)
# print(f'Okay {name} welcome to PYTHON!')


#             IF STATEMENTS           (checks to see if a condition is true and run, if it's not then run the option)
# age = 16
# if age > 16:
#     print('you should be driving by now')
# elif age == 16:
#     print('can now drive')
# else:
#     print('can not drive')



# #                      NESTED IF STATEMENT
# gender = 'male'
# age = 21
#
# if age >= 21:
#     if gender == 'male':
#         print (f'age is {age} and gender is {gender}')
#     else:
#         print(f'age is {age} but gender is not {gender}')
# else:
#     print(f'age is not {age}')



#               FOR LOOPS             (used to iterate through a list and maybe pick them or do something with them)
# names = ['Daniel', 'Joseph', 'John', 'Joy', 'Sarah']

# if 'Daniel' in names:
#     print("Daniel is part of the list")
# else:
#     print("Invalid name!")

# for name in names:
#     print(name, "is my favorite")

# for name in names[1:3]:
#     print(name, "these are the best")

# for name in names:
#     if name == 'Daniel':
#         print(f"{name}. Stopped count since {name} is found")
#     else:
#         print("name not found")
#     break


#               WHILE LOOPS             (Loops that runs WHILE a condition is true)
# numbers = [1,2,8,7,3,4,0,3,1]
# nums = 1
# count = 1
#
# while nums < (len(numbers)):
#     print(f"{nums} is lesser than the length of numbers: {count}")
#     nums += 1
#     count += 1
#     if nums == len(numbers):
#         print(f"{nums} is now equal to the length of numbers, so loop stopped")
#
# year = 4000
# century = 100
#
# while century < year:
#     if century % 3 == 0:
#         print(century)
#     century += 100
#     if century >= 1950:
#         break


#            RANGE         (generate list of numbers which can be used to iterate over using for loops)

# for n in range(10 + 1):
#     print(n)

# for n in range(4,10):
#     print(n)

# for n in range(0,10,2):
#     print(n)

# cars = ['Toyota', 'Audi', 'Subaru', 'Mercedes', 'BMW', 'Telsa', 'Ford']
# #
# for car in range(len(cars)):
#     print(f'index:{car} is {cars[car]}')
#     car += 1
# print(f'total length of cars is {len(cars)}')



#            FUNCTION         (this is  block of code that can be used and called upon later in our app)
# def greet(time,city, name='Emmy' ):  #creating the function
#     print(f"Hello I am {name} and it's {time} now in {city}")
#
# name = input(print('type your name:'))
# city = input(print('type your city:'))
#
# greet(time='Noon', city=city, )   #calling the function (function can also be called many times).

# def find_max(numbers):
#     """
#     Function to find the maximum number in a list.
#
#     Parameters:
#         numbers (list of int or float): List of numbers.
#
#     Returns:
#         int or float: Maximum number in the list.
#     """
#     if not numbers:
#         return None
#     return max(numbers)


# # Test the function
# numbers_list = [0]
# if len(numbers_list) == 0:
#     print("0")
# else:
#     max_number = max(numbers_list)
#     print(f"The maximum number in the list {numbers_list} is: {max_number}")


# Variable Scope(Global and Local)


#                                  List
# states = ['Lagos', 'Kano', 'Kaduna', 'Ogun', 'Oyo', 'Osun', 'Ondo', 'Ekiti', 'Kwara', 'Kogi', 'Benue', 'Nasarawa', 'Plateau', 'Taraba', 'Adamawa', 'Bauchi', 'Gombe', 'Yobe', 'Borno', 'Jigawa', 'Katsina', 'Zamfara', 'Sokoto', 'Kebbi', 'Niger', 'FCT']
# print(states[10])        # used to get the 10th item in the list
# print(states[-1])        # used to get the last item in the list   (- means counting from the end)
# print(states[1:5])       # used to get a range of items in the list
# print(states[:5])        # used to get all items from the beginning to the 5th item
# states[5] = 'changed'       # used to get all items from the 5th item to the end
# print(states[5])
# print(len(states))         # used to get the length of the list
# print(states.index('Kano'))    # used to get the index of an item in the list
# states.append('Nigeria')    # used to add an item to the end of the list
# added_state = states.insert(0, 'Nigeria')   # used to add an item to a specific index in the list
# print(states[0])
# states.extend(['Canada', 'London', 'Liverpool'])   # used to add multiple items to the end of the list
# print(states)
# states.append(['Tunisia', 'Tokyo', 'Ohio'])   # used to add a list as an item to the end of the list
# print(states)


# fruits = ['apple', 'banana', 'cherry']
# vegetables = ['carrot', 'potato', 'onion']
#
# fruits_vegetables = [fruits, vegetables]
# print(fruits_vegetables)



#                         DICTIONARIES(A MAPPING TYPE, SET OF KEY VALUE PAYS)    USE THE KEY TO GET THE VALUE.
# computers = {'HP':'Hardware', 'Intel':'Linux', 'AMD':'Android'}
# print(computers['HP'])
#
# for key, value in computers.items():
#     print(f'{key}: {value}')
#
# if 'macOS' in computers:
#     print('macOS found')
#     print()
# else:
#     print('MacOS not found.')



#                                  TUPLES
# TUPLES are immutable list that can not be modified or changed.   so we use tuples when we want a fixed list.
# my_tuples = (10, 5, 3, 6, 7, 3)
#
# print(my_tuples[0])
# my_tuples[3] = 50   #  this will throw error.
# print(my_tuples)



#                                                                SETS & SORTING
#  SORT: IT SORT LIST NUMERICALLY, LOWEST COME FIRST AND HIGHEST COMES LAST.
# my_num_list = [4,2,6,3,8,2,9,3,6,3,5,2,8,45,3]
# my_alpha_list = ['zaria', 'mango', 'apple', 'toyota', 'bus', 'bird', 'human', 'space']
# my_alpha_list_second = ['zaria', 'mango', 'apple', 'space', 'Texas', 'toyota', 'bus', 'Laptop', 'bird','apple', 'human', 'Telsa', 'space']
# #  Capital letter always comes first.

# sorted_nums = sorted(my_alpha_list_second)
# print(sorted_nums)

# #SET:  THIS IS A COLLECTION OF DATA JUST LIKE LIST AND MAPS, HOWEVER THEY DO NOT ALLOW DUPLICATE
# set_nums = set(my_num_list)
# print(set_nums)


# my_dict = {'language': 'Python', 'name': 'FlutterDevGuy', 'work': 'Developer', 'laptop': 'Macbook', 'language': 'Python', 'phone': 'Iphone', 'laptop': 'Macbook'}
# dict_values = my_dict.values()
# print(dict_values)
# print (set(dict_values))



# #                           Classes
# class Student:
# #     #CLS: access to the whole class
# #     #SELF: access to individual instance
# # #  N.B:   how instance methods and attributes, class attributes and methods, static method can be accessible or available to
# # #  Instance are available on the Instance only, Class level available on the instance and class, and also static method which are available on instance and class itself, and takes only the params passed in it.

#     #CLASS VARIABLES/ATTRIBUTE.        MUST BE INITIALIZED AND ALSO ACCESSIBLE TO ALL INSTANCE OF THE CLASS
#     school = 'Veechies'
#     resume = 'School resumes by 7:45 AM'
#     numbers_of_student = 0


    # def __init__(self, age, name, hobby):
    #     # INSTANCE VARIABLES/ATTRIBUTE.                  ACCESSIBLE TO ONLY INSTANCE OF THE CLASS
    #     self.age = age
    #     self.name = name
    #     self.hobby = hobby

#     # INSTANCE METHODS                                  ACCESSIBLE TO ONLY INSTANCE OF THE CLASS
#     def get_age_name(self):
#         return f'name of student is {self.name}, and student is {self.age}'

#     #CLASS METHODS                               ACCESSIBLE TO BOTH THE CLASS ITSELF AND ALL INSTANCE OF THE CLASS
#     @classmethod
#     def class_function(cls):
#         return f'this is a class function so i can get access to the school which is {cls.school}'
    
#     #STATIC METHODS.        this method does not have access to self or the class itself, it only has access to the params pass into it individually
#     @staticmethod
#     def terms(semester = '3 terms a year'):
#         return f'the school is open {semester} every year'
            

#Student.numbers_of_student += 1
# student_1 = Student(14, 'Ade', 'Soccer')
# student_2 = Student(15, 'Derby', 'Dancing')

# print(student_1.class_function())
# print(Student.terms())
# print(Student.terms('2 terms a year'))   # this overrides the initial value for the param
# print(Student.numbers_of_student)
# print(student_1.age, student_1.name)
# print(student_2.age)
# print(student_1.get_age_name())
# print('student 2 school is', student_2.school)
# print('All student school is', Student.school)



#                                             MODULES AND PACKAGES
# MODULES:  These are python file that could be called upon, imported, and used. in this case, (the student class in the problems.py file)
# PACKAGES:  These are collection of modules.  (instead of putting too much functionality in one module, split it out to different modules, and all of those modules will be in one package)

# from cars_packages.car import Car
# from cars_packages.car_module_one import CarColor
#
# car_1 = Car('Toyota', 'Petrol', 'Japan')
# car_2 = Car('Tesla', 'Electric', 'USA')
#
#
#
# print(car_2.name)
# print(f'i am car_2 and all cars color are fixed as {CarColor.all_color}')
# print(car_2.drive())




#                                             LIST COMPREHENSION
#              This gives us alternative ways to construct list or dictionaries based on other collections.

#my_list = [20, 4, 6, 7, 3, 6, 8, 9, 2, 6]

# # your_list = [what you want to return/ output, what you want to circle/ loop through]
# # your_list = [what you want to return/ output, what you want to circle/ loop through, any conditions you want to carry]
# double_list = [num * 2 for num in my_list]
# print(double_list)

# squared_list = [num ** 2 for num in my_list if num % 2 == 0]
# print(squared_list)

# def checking():
#     check_list  = [num ** 2 for num in my_list if num % 2 == 0]
#     return check_list

# print(checking())

# list_comp = [num ** 2 if num % 2 == 0 else num for num in my_list]  # returns all  numbers but square only even numbers
#list_comp = [num + 1 if num % 2 == 1 else num for num in my_list]  # returns all  numbers but make odd numbers even
#print(list_comp)



#                                              FILTERS
#   Filters is an easy way to take a collection and filters out some of it values based on a function result and this give us a new filter collection
# my_list = ['A', 'C', 'F', 'F', 'D', 'B', 'E', 'D', 'F']
#
# def remove_fails(passed):
#     return passed != 'F'
#
# #new_list/string = list(filter(testing_function, list))
# passed_list = list(filter(remove_fails, my_list))
# print(passed_list)



#                                           MAPS
# Takes in a function as first params and iterable as second params. then return an iterator that applies the function to every item of the iterable

# def make_even(x):               # returns all  numbers but square only even numbers
#     if x & 2 == 1:
#         return x + 1
#     else:
#         return x
#
# def square(x):
#     return x ** 2
#
#
# numbers = [1, 2, 3, 4, 5, 7, 3, 9, 0, 2]
#
# # Use map() to apply the square function to each number in the list
# square_list = list(map(square, numbers))
# make_even_list = list(map(make_even, numbers))
#
# print(square_list)
# print(make_even_list)



#                                            LAMBDAS
#   Lambda functions does not have a name and use to return values.
#   Lambda functions are short, nameless functions used for quick tasks in Python, and are used just once.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# squared_list = list(map(lambda n: n ** 2, nums))
# even_numbers = list(filter(lambda x: x % 2 == 0, nums))
# print(squared_list)
# print(even_numbers)


#                                  DECORATORS


#                                                RANDOM

# import random

# random_number = random.randint(1, 10)
# print(random_number)

# random_number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(random_number)

# random_number = random.random() * 100
# print(random_number)

# love_score = random.randint(1, 100)
# print(f'your love score is {love_score}%')


#                                             Reading Files
# ipsum_file = open('text_files/ipsum_text_file.txt')
# # for line in ipsum_file:
# #     print(line.rstrip())
#
# ipsum_file.seek(0)
# lines = ipsum_file.readlines()
# print(lines)
#
# ipsum_file.seek(10)                    # find the 30th character in the files
# file_text = ipsum_file.read(50)              #then read 20 characters from the point
# print(file_text)
#
# ipsum_file.close()                         # always remember to close show it does not add anything below.

# def sequence_filter(filtered_line):
#     return filtered_line[0] != '>'
#     #return '>' not in filtered_line
#
# with open('text_files/dna_text_file.txt') as dna_file:
#     # for line in dna_file:
#     #     if line[0] != '>':
#     #         print(line.rstrip())
#     filtered_line = list(filter(sequence_filter, dna_file))
#     print(filtered_line)                               #  now we don't have to close this.




#                                   Write to a File
# with open('text_files/write.txt', 'w') as write_file:          #   opening are read online so we add the ('w') to write.
#     write_file.write('I have just written this line to the file')
#     write_file.write('\nI have just written this second line to the file and added here')
#
#
# with open('text_files/write.txt', 'a') as write_file:  # we use ('a') to amend. o it does not have to delete other line in the file
#     write_file.write('\nI have just written this line to the file')
#     write_file.write('\nI have just written this second line to the file and added here')
#
# quotes = [
#     '\nI have just added this quote line 1 to the file and added here'
#     '\nI have just  added this quote line 2 to the file and added here'
#     '\nI have just  added this quote line 3 to the file and added here'
# ]
#
#
# with open('text_files/write.txt', 'a') as write_file:
#     write_file.writelines(quotes)