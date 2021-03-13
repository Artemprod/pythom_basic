users_number = int(input("set your number: "))

# тут 2 варинат какой из них лучше ?
# 1 вариант

# a = users_number % 10
# b = users_number // 10
# list_1 = [a]
#
# while b > 0:
#     a = b % 10
#     b = b // 10
#     list_1.append(a)
# print(list_1)
# print(max(list_1))

# ___________________________________

# 2 вариант

# a = users_number % 10
# b = users_number // 10
# re = b % 10
#
# m = 0
# if a > re:
#     m = a
# else:
#     m = re
#
# while b > 0:
#     a = b % 10
#     b = b // 10
#     re = b % 10
#
#     if a > re:
#         if m < a:
#             m = a
#         else:
#             m
#     if a < re:
#         if m < re:
#             m = re
#         else:
#             m
#
# print('max number is: ', m)
