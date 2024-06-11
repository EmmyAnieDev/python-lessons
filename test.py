
# import random
#
# inputs = []
# for i in range(50):
#     inputs.append(random.randint(1, 1000))
#
# largest_num = 0
# for num in inputs:
#     if num > largest_num:
#         largest_num = num
#
#
# print(largest_num)


name = 'william'


name_as_list = list(name)
print(name_as_list)
left = 0
right = len(name_as_list) - 1

reversed_name = ''

while right >= left:
    reversed_name += name_as_list[right]
    right -= 1

print(reversed_name)