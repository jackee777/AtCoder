A, B, N = map(int, input().split())

l = 0
r = 10 ** 9 + 1
while (r - l) > 1:
    m = (l + r) // 2
    M = A * m + B * len(str(m))
    if M <= N:
        l = m
    else:
        r = m
print(l)
