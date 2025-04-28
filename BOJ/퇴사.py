N = int(input())

schedule = [0]

for _ in range(N):
    t, p = map(int, input().split())
    schedule.append((t, p))
    
dp = [-1 for _ in range(N+1)]

for i in range(N, 0, -1):
    if i+schedule[i][0] > N+1:
        dp[i] = 0
    else:
        dp[i] = schedule[i][1]
        break

def func(n):
    #print(n)
    if n == N+1:
        return 0
    if dp[n]!=-1:
        return dp[n]
    
    if n + schedule[n][0] <= N+1:
        dp[n] = schedule[n][1] + func(n+schedule[n][0])
        
    dp[n] = max(dp[n], func(n+1))
    return dp[n]

func(1)
print(dp[1])
