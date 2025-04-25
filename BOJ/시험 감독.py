import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = N

for a in A:
    a-= B
    if a <= 0:
        continue
    
    ans+= (a//C)
    if (a%C != 0):
        ans+=1
        
print(ans)
