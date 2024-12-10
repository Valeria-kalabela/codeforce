n=int(input())
mas=[]
ans=0
for i in range(0,n):
    mas.append(int(input()))
mas.sort()
for i in range(0,n-1):
    ans+=mas[i]+1
ans+=2
print(ans)