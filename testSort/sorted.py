# a = {'a': 552, 'b': 457, 'c': 785, 'd': 211}
#
# for v, k in sorted(zip(a.values(), a.keys())):
#     print(k, v)
""""""
# 3)
# import re
# a = 'sd5 3b5hj b53j 34'
# numb = [int(f) for f in re.findall('\d+', a)]

# print(numb)

# import re
# a = 'sd5 3b5hj b53j 34'
# # numb = [int(f) for f in re.findall('\d+', a)]
# numb = [f for f in re.findall('\D+', a)]
# print(numb)

# 1)
# import re
# a = 'fjnn5k34n j34 3j4 3j3 45'
# nums = re.findall('[0-9]+', a)
# b = []
# print(nums)
# for f in nums:
#     b.append(int(f))
# print(b)

# 2)
# b = []
# temp = ''
# for f in a:
#     if f.isdigit():
#         temp += f
#     elif temp:
#         b.append(int(temp))
#         temp = ''
# if f.isdigit():
#     b.append(int(f))
# print(temp)
# print(b)
""""""