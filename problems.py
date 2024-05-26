# my_list = [2, 5, 8, 4, 9, 3, 8, 4, 9, 2, 1, 5, 7, 3, 5]

# def sum_of_my_lists(my_list):
#     total = 0
#     for i in my_list:
#         total += i
#     print(total)

# sum_of_my_lists(my_list)

# my_list = [2, 5, 8, 4, 9, 3, 8, 4, 9, 2, 1, 5, 7, 3, 5]
# def print_max_in_list(my_list):
#     max_value = max(my_list)
#     return max_value
#
#
# result = print_max_in_list(my_list)
# print(result)

my_list = [2, 5, 8, 4, 9, 3, 8, 4, 9, 2, 1, 5, 7, 3, 5]

print(2 in my_list)

if 2 in my_list:
    print('yes')
else:
    print('no')

# my_list = [1, 2, 3, 4, 5, 5, 7, 2, 9, 0, 2, 6]
#
# def count_even_numbers(my_list):
#
#     count = 0
#     for num in my_list:
#         if num % 2 == 0:
#             count += num
#     return count
#
# result = count_even_numbers(my_list)
# print(result)


# my_list = [1, 2, 3, 4, 5, 5, 7, 2, 9, 0, 2, 6]

# def return_even_numbers(my_list):
#     even_numbers = []
#     for num in my_list:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# result = return_even_numbers(my_list)
# print(result)

# my_list = [1, 6, 2, 9, 3, 4, 5, 5, 7, 2, 9, 0, 2, 6]

# def nums(my_list):
#     squared_nums = []
#     for num in my_list:
#         squared_num = num ** 2
#         squared_nums.append(squared_num)
#     return squared_nums

# result = nums(my_list)
# print(result)


# my_string = "H,E,L,L,O"

# def reverse_string(my_string):
#     left = 0
#     right = len(my_string)-1
#
#     while left < right:
#         left = right
#         right = left
#
#         left += 1
#         right -= 1
#     return my_string
#
# result = reverse_string(my_string)
# print(result)

# numbers = [1,2,3,4,5,6,7,8,9,10]

# for nums in numbers:
#     squared_even_numbers = []
#     if nums % 2 == 0:
#         squared_nums = nums ** 2
#         squared_even_numbers.append(squared_nums)


# print(squared_even_numbers)


#                                                            Using a function
# my_list = [2, 3, 5, 6, 7, 6, 9]

# squared_even_numbers = []

# def square(my_list):
#     for nums in my_list:
#         if nums % 2 == 0:
#             squared_nums = nums ** 2
#             squared_even_numbers.append(squared_nums)
#     return squared_even_numbers
        
# print(square(my_list))


#                               filtering

#my_list = ['A', 'C', 'F', 'F', 'D', 'B', 'E', 'D', 'F']

# pass_list = []
# for item in my_list:
#     if item != 'F':
#         pass_list.append(item)
# print(pass_list)

# pass_list = [item for item in my_list if item != 'F']
# print(pass_list)


# result = 25
#
# if result < 18.5:
#     print('person is under weight')
# elif result < 25:
#     print('person is normal weight')
# elif result < 30:
#     print('person is slightly overweight')
# elif result < 35:
#     print('person is obese')
# else:
#     print('person is clinically obese')
#


#                       Random
# import random
# #
# # random_side = random.randint(0, 1)
# #
# # if random_side == 1:
# #     print("you won")
# # else:
# #     print("you lost")
#
# people = ["Emmy", "John", "Doe", "Jane"]
#
# random_person = random.choice(people)
# print(random_person + " is going to buy the meal today")


#                                     FOR LOOP
# students_heights = [180, 124, 165, 173, 189, 169, 146, 178]
#
# sum_of_students_height = 0
# for item in students_heights:
#     sum_of_students_height += item
# print(sum_of_students_height)
#
# average_height = sum_of_students_height // len(students_heights)
# print(average_height)


# sum_of_students_height = sum(students_heights)
# print(sum_of_students_height)
#
# average_height = sum_of_students_height // len(students_heights)
#
# print(average_height)

#
# for number in range(1, 100 + 1):
#     if number % 3 == 0:
#         print('Fuzz')
#     elif number % 5 == 0:
#         print('Buzz')
#     elif number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     else:
#         print(number)

#                                                            Random
# import random
#
# word_list = ['ardvark', 'baboon', 'camel']
#
# chosen_word = random.choice(word_list)
# print(f'the chosen word is: {chosen_word}')
#
# guess = input('Guess a letter: ').lower()
#
# for letter in chosen_word:
#     if letter == guess:
#         print(True)
#     else:
#         print(False)


# #                                    While loop
#
# numbers = [3, 7, 4]
# user_answer = input('Do you wanna play? (Y/n) ')
#
# while user_answer != 'n':
#     user_input = int(input('guess a number in the list: '))
#     if user_input in numbers:
#         print('you got a number correctly!')
#         break
#     else:
#         print('you chose a wrong number!')
#     user_answer = input('Do you wanna play again? (Y/n) ')



#                              Dictionaries
#list of dictionaries

# friends = [
#     {'name': 'Ekene', 'age': 20, 'state': 'Lagos'},
#     {'name': 'Chris', 'age': 23, 'state': 'Uyo'},
#     {'name': 'Boss', 'age': 25, 'state': 'Texas'},
# ]
#
# person = {'Ekene': 20, 'Chris': 23, 'Boss': 25}
#
# print(friends[2]['name'])
# print(sum(person.values()) / len(person.values()))


# #                                    LAMBDA
#
# add = lambda x, y: x + y
# print((lambda x, y: x * y)(5, 7))
#
# print(add(5, 7))



#                            CLASS...     INHERITANCE
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def disconnect(self):
        self.connected = False
        print('Disconnected.')


#         Add the superclass name in a parenthesis inside the subclass
class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"Printer Name: {self.name}, Connection Type: {self.connected_by}, {self.remaining_pages} remaining pages"

    def print_pages(self, pages):
        if not self.connected:
            print('Your Printer is not connected')
        else:
            print(f'printing {pages} pages.')
            self.remaining_pages -= pages

my_printer = Printer('Printer', 'USB', 500)
my_printer.print_pages(20)
print(my_printer)
my_printer.disconnect()
my_printer.print_pages(20)