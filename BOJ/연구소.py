N, M = map(int, input().split())

init_lab = []
safe_zone = 0
init_birus = []
for i in range(N):
    row = list(map(int, input().split()))
    init_lab.append(row)
    for j in range(M):
        if row[j] == 0:
            safe_zone+=1
        elif row[j] == 2:
            init_birus.append((i, j)) 
safe_zone-=3

ans = 0

def bfs():
    global safe_zone, ans
    queue = list(init_birus)
    lab = list(map(list, init_lab))
    new_birus = 0
    
    while(queue):
        (x, y) = queue.pop()
        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            
            if not (0<=nx<=N-1 and 0<=ny<=M-1):
                continue
            
            if lab[nx][ny] == 0:
                lab[nx][ny] = 2
                queue.append((nx, ny))
            
                new_birus+=1
                if safe_zone - new_birus <= ans:
                    return
                
    ans = safe_zone - new_birus

def construct(x, y, cnt):
    while True:
        if cnt==3:
            bfs()
            return
        
        if not (x<=N-1 and y<=M-1):
            break
        
        if init_lab[x][y] == 0:
            init_lab[x][y] = 1
            construct(x, y, cnt+1)
            init_lab[x][y] = 0
            
        if y==M-1:
            x+=1
            y=0
        else:
            y+=1

construct(0, 0, 0)
print(ans)
