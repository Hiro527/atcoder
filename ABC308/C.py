n = int(input())
l = {}

for i in range(n):
    a, b = map(int, input().split())
    p = a / (a + b)
    l[i] = p

s = list(map(lambda x: x[0]+1, sorted(l.items(),
         key=lambda x: (x[1], x[0]), reverse=True)))

print(*s)

# 4WA
