t=int(input())
n=int(input())
mt,mn=[],[]
ans=0
time=0
for i in range(0,t):
    mt.append(int(input()))
for i in range(0,n):
    mn.append(int(input()))
if n==1:
    time=mn[0]
    if time<=t:  ans+=sum(mt[time:t+1])
print(ans+1)