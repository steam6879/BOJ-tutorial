# # 10871
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# result = []
#
# for i in range(n):
#     if a[i] < x:
#         result.append(a[i])
#
# print(' '.join(map(str, result)))

# # 2562
# a = []
# for i in range(9):
#     a.append(int(input()))
#
# print(max(a))
# print(a.index(max(a)) + 1)

# 10810
basket_num, n = map(int, input().split())
basket = [0] * basket_num

for i in range(n):
    start_num, end_num, key = map(int, input().split())
    for j in range(start_num - 1, end_num):
        basket[j] = key

print(' '.join(map(str, basket)))