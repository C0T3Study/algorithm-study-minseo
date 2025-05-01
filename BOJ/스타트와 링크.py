import sys
input = sys.stdin.readline

N = int(input())
stat = []

for _ in range(N):
    stat.append(list(map(int, input().split())))
team_start = [False for _ in range(N)]    

ans = 10e9
def calculate_stat():
    global ans
    s = []
    l = []
    for n in range(N):
        if team_start[n] == True:
            s.append(n)
        else:
            l.append(n)
    
    stat_s = 0
    for i in s:
        for j in s:
            if not i==j:
                stat_s+=stat[i][j]
    stat_l = 0
    for i in l:
        for j in l:
            if not i==j:
                stat_l+=stat[i][j]
    
    ans = min(ans, abs(stat_s - stat_l))
            
    

def pick(index, cnt):
    while True:
        if cnt == N//2:
            calculate_stat()
            return
        if index >= N:
            return
        
        if team_start[index] == False:
            team_start[index] = True
            pick(index+1, cnt+1)
            team_start[index] = False
        index+=1

pick(0, 0)
print(ans)
