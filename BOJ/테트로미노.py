import sys
input = sys.stdin.readline

N, M = map(int, input().split())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

visited = [[False]*M for _ in range(N)]

def dfs(blocks, size, part_sum):
    global ans
    
    if size >= 4:
        ans = max(ans, part_sum)
        return
    
    for block in blocks:
        x, y = block[0], block[1]
    
        for (dx, dy) in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx = x + dx
            ny = y + dy
            
            if (not 0<=nx<=N-1) or (not 0<=ny<=M-1):
                continue
            if visited[nx][ny]:
                continue
                print(nx, ny)
            visited[nx][ny] = True
            dfs(blocks+[(nx, ny)], size+1, part_sum + paper[nx][ny])
            visited[nx][ny] = False
        
ans = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs([(i,j)], 1, paper[i][j])
    
print(ans)
