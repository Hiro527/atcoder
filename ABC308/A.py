s = list(map(int, input().split()))

if s != sorted(s):
    print('No')
    exit()
else:
    for i in s:
        if 100 <= i and i <= 675 and i % 25 == 0:
            pass
        else:
            print('No')
            exit()
    else:
        print('Yes')
