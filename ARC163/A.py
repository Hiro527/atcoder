t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    f = False
    for j in range(1, n):
        a = s[:j]
        b = s[j:]
        if a < b:
            f = True
    print('Yes' if f else 'No')
