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

result = 25

if result < 18.5:
    print('person is under weight')
elif result < 25:
    print('person is normal weight')
elif result < 30:
    print('person is slightly overweight')
elif result < 35:
    print('person is obese')
else:
    print('person is clinically obese')
