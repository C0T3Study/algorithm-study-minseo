import sys
input = sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append((int(input()), i))

sorted_A = sorted(A)

res = 0

for i in range(N):
    res = max(res, sorted_A[i][1] - i)
    
print(res+1)
