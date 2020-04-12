import collections
N = int(input())
S = input()
c = collections.Counter([s for s in S])
RGB = c.most_common()
if len(RGB) != 3:
    result = 0
else:
    rgb = set(["R", "G", "B"])
    result = RGB[0][1] * RGB[1][1] * RGB[2][1]
    for i in range(1, N//2+1):
        for j in range(N-i*2):
            if set([S[j], S[j+i], S[j+i*2]]) == rgb:
                result -= 1
print(result)
