n=int(input())
mas=[]
ans=0
for i in range(0,n):
    mas.append(int(input()))
for i in range(0,n+1):
    for j in range(i+1,n+1):
        if i==0 and j!=n:
            ans=max(abs(sum(mas[i:j])-sum(mas[j:n])),ans)
        if j==n and i!=0:
            ans=max(abs(sum(mas[0:i])-sum(mas[i:j])),ans)
        elif i!=0 or j!=n:
            ans=max(abs(sum(mas[i:j])-sum(mas[j:n])),abs(sum(mas[0:i])-sum(mas[i:j])),ans)
print(ans)