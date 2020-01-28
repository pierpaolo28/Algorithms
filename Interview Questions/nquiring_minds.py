a = [1, 2, 3, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = 2

print(a[::-1])

res = []
for i in range(len(a)-1, 0, -1):
    if a[i] >= t:
        res.append(i)
    else:
        break

print(res)