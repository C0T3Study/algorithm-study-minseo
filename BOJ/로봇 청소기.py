import sys
input = sys.stdin.readline

N, M = map(int, input().split())
x, y, d = map(int, input().split())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))
ans = 0

def move(x, y, d):
    if d == 0:
        return x-1, y 
    elif d == 1:
        return x, y+1
    elif d == 2:
        return x+1, y
    elif d == 3:
        return x, y-1

def clean(x, y):
    global ans
    if room[x][y] == 0:
        room[x][y] = -1
        ans+=1
    
while True:
    clean(x, y)
    
    nx, ny = x, y
    cleaned = False
    for _ in range(4):
        d = (d+3)%4
        nx, ny = move(x, y, d)
        
        if not (0<=nx<=N-1 and 0<=ny<=M-1):
            continue
        
        if room[nx][ny] == 0:
            x, y = nx, ny
            clean(x, y)
            cleaned = True
            break
    
    if not cleaned:
        nx, ny = move(x, y, (d+2)%4)
        
        if (0<=nx<=N-1 and 0<=ny<=M-1) and room[nx][ny] != 1:
            x, y = nx, ny
            continue
        else:
            break

print(ans)
