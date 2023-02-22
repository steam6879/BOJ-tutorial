# #10871
# n, x = map(int, input().split())
# a = list(map(int, input().split()))
# result = []
#
# for i in range(n):
#     if a[i] < x:
#         result.append(a[i])
#
# print(' '.join(map(str, result)))

#2562
a = []
for i in range(9):
    a.append(int(input()))

print(max(a))
print(a.index(max(a)) + 1)