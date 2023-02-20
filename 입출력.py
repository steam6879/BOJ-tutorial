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

# #3003
# user_input = input()
# numbers = [int(num) for num in user_input.split()]
#
# piece = [1, 1, 2, 2, 2, 8]
# n = len(piece)
# modifing_piece = [0] * n
#
# for i in range(6):
#     if numbers[i] == piece[i]:
#         modifing_piece[i] = 0
#     else:
#         modifing_piece[i] = piece[i] - numbers[i]
#
# print(' '.join(str(s) for s in modifing_piece))

# #3003 - using map function
# chess = [1, 1, 2, 2, 2, 8]
#
# a = list(map(int, input().split()))
#
# for i in range(len(a)):
#     print(chess[i] - a[i], end=' ')

# #2588 - 나머지를 구하는 %을 이용하여 값을 바로 출력하는 방법    Fail
# num1 = int(input())
# num2 = int(input())
#
# print(num1 * (num2%10))
# print(num1 * ((num2%100)//10))
# print(num1 * (num2//100))
# print(num1 * num2)

#2588 - 결과값을 list 변수에 담고, 출력하는 방법   Fail
num1 = int(input())
num2 = list(map(int, input()))

result = []

for i in range(len(num2), 0, -1):
    result.append(num1 * num2[i - 1])

print(result[0], result[1], result[2], sep='\n')
print(result[0] + (result[1]*10) + result[2] * 100)
