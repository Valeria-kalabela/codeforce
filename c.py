p = int(input())
q = int(input())
n = q - p + 1
ans = 0
if p == q:
    ans = 1
elif p==1:
    for i in range(1, n):
        ans = ans + (1 + i) * i // 2
    ans+=n
else:
    for i in range(1, n + 1):
        ans = ans + (1 + i) * i // 2
print(ans)