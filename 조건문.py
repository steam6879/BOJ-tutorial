# #2753
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(1)
#
# else: print(0)

# #14681
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print(1)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)
# else: print(4)

# #2884
# (hour, min) = tuple(map(int, input().split()))
#
# if hour != 0:
#     if min < 45:
#         (hour, min) = (hour - 1, 15 + min)
#     else:
#         (hour, min) = (hour, min - 45)
# else:
#     if min < 45:
#         (hour, min) = (23, 15 + min)
#     else:
#         (hour, min) = (hour, min - 45)
#
# print(hour, min)

# #2525
# hour, min = map(int, input().split())
# timer = int(input())
#
# if (min + timer) < 60:
#     print(hour, min + timer)
# else:
#     if (hour + (min + timer) // 60) >= 24:
#         print((hour + (min + timer) // 60) - 24, (min + timer) % 60)
#     else:
#         print((hour + (min + timer) // 60), (min + timer) % 60)

#2480 - fail
a, b, c = map(int, input().split())

if a == b and b == c:
    print(10000 + a * 1000)

elif a == c or a == b:
    print(1000 + a * 100)

elif b == c:
    print(1000 + b * 100)

else:
    print(max(a, b, c) * 100)

