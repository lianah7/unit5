# by Liana Hill
# last updated October 18, 2019
# daily exercises - unit 5

import random

# # number one
# user_upper - 1 includes the chosen value as it counts down
# print("Please pick numbers that make sense")
# user_upper = int(input("Enter a number for the upper value"))
# user_lower = int(input("Please enter a value for the lower value"))
# for x in range(user_lower, user_upper + 1):
#     print(x)
# if user_upper < user_lower:
#     for x in range(user_lower, user_upper - 1, -1):
#         print(x)

# # number two
# for x in range(10, 21):
#     print(x)
#
# for x in range(2, 42, 2):
#     print(x)

# # problem three
# user_positive_integer = int(input("Please enter a positive number"))
# for x in range(13):
#     print(user_positive_integer, '*', x, '=', user_positive_integer * x)

# # number four
# even_sum = 0
# odd_sum = 0
# for x in range(10):
#     random_number = (random.randint(1, 100))
#     print(random_number)
#     if random_number % 2 == 0:
#         even_sum = even_sum + random_number
#     else:
#         odd_sum = odd_sum + random_number
# print("The sum of the even numbers is", even_sum)
# print("The sum of the odd numbers is", odd_sum)

# # number five
# multiples = 0
# for x in range(3, 1000):
#     if x % 3 == 0 or x % 5 == 0:
#         multiples = multiples + x
# print("The sum of all the multiples of three and five is", multiples)

# # number six
# user_num =  int(input("Please pick a number to make a right triangle"))
# number_stars = "* "
# for x in range(user_num + 1):
#     print(number_stars * x)

# # number seven
# tries = 0
# total = 0
# product = 1
# while True:
#     user_int = (input("Please enter a number"))
#     if user_int == "q":
#         break
#     user_int = int(user_int)
#     tries += 1
#     total = total + user_int
#     product = product * user_int
#
# print("The average is of your numbers is", total / tries, "and the product is", product)


# number eight
steps = 0
user_num = int(input("Enter a number"))
while user_num != 1:
    if user_num % 2 == 0:
        even = user_num / 2
        user_num = even
        print(user_num, "->", user_num / 2, "=", even)
    else:
        odd = user_num * 3 + 1
        user_num = odd
        print(user_num, "->", user_num * 3 + 1, "=", odd)
    steps += 1
print("It took you", steps, "steps to get to one")












