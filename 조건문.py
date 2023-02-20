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

#2884
(hour, min) = tuple(map(int, input().split()))

if hour != 0:
    if min < 45:
        (hour, min) = (hour - 1, 15 + min)
    else:
        (hour, min) = (hour, min - 45)
else:
    if min < 45:
        (hour, min) = (23, 15 + min)
    else:
        (hour, min) = (hour, min - 45)

print(hour, min)