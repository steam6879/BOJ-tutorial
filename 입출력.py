# #1000
# a, b = input().split()
#
# print(int(a) + int(b))

# #10926
# id = input()
#
# print(id + "??!")

# #18108
# year = int(input())
# print(year - 543)

#3003
user_input = input()
numbers = [int(num) for num in user_input.split()]

piece = [1, 1, 2, 2, 2, 8]
n = len(piece)
modifing_piece = [0] * n

for i in range(6):
    if numbers[i] == piece[i]:
        modifing_piece[i] = 0
    else:
        modifing_piece[i] = piece[i] - numbers[i]

print(' '.join(str(s) for s in modifing_piece))