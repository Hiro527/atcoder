n, m = map(int, input().split())
c = list(input().split())
d = list(input().split())
p = list(map(int, input().split()))

ans = 0

for i in range(n):
    color = c[i]
    if color in d:
        ans += p[d.index(color) + 1]
    else:
        ans += p[0]

print(ans)