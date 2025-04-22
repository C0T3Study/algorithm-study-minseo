N, M = map(int, input().split())

maze = []
for i in range(N):
    row = input()
    maze.append(row)
    for j in range(M):
        if maze[i][j] == 'R':
            red = [i, j]
        if maze[i][j] == 'B':
            blue = [i, j]

def move(red, blue, direction, cnt):
    global ans
    
    if cnt > 10:
        return
    
    rx, ry = red[0], red[1]
    bx, by = blue[0], blue[1]
    
    if direction == 'up':
        while (bx > 0):
            if maze[bx-1][by] == 'O':
                return # 파란 구슬이 들어가 실패
            elif maze[bx-1][by] == '#':
                break
            bx-=1
        
        while (rx > 0):
            if maze[rx-1][ry] == 'O':
                ans = min(ans, cnt)
                return # 성공
            elif maze[rx-1][ry] == '#':
                break
            rx-=1
        
        if (rx, ry) == (bx, by): #구슬이 붙어있는 경우
            # 본래 아래에 있던 구슬을 아래로 한 칸 이동
            if red[0] > blue[0]:
                rx+=1
            elif red[0] < blue[0]:
                bx+=1
    
    elif direction == 'down':
        while (bx < N-1):
            if maze[bx+1][by] == 'O':
                return # 파란 구슬이 들어가 실패
            elif maze[bx+1][by] == '#':
                break
            bx+=1
        
        while (rx < N-1):
            if maze[rx+1][ry] == 'O':
                ans = min(ans, cnt)
                return # 성공
            elif maze[rx+1][ry] == '#':
                break
            rx+=1
        
        if (rx, ry) == (bx, by): #구슬이 붙어있는 경우
            # 본래 위에 있던 구슬을 위로 한 칸 이동
            if red[0] < blue[0]:
                rx-=1
            elif red[0] > blue[0]:
                bx-=1
                
    elif direction == 'left':
        while (by > 0):
            if maze[bx][by-1] == 'O':
                return # 파란 구슬이 들어가 실패
            elif maze[bx][by-1] == '#':
                break
            by-=1
        
        while (ry > 0):
            if maze[rx][ry-1] == 'O':
                ans = min(ans, cnt)
                return # 성공
            elif maze[rx][ry-1] == '#':
                break
            ry-=1
        
        if (rx, ry) == (bx, by): #구슬이 붙어있는 경우
            # 본래 오른쪽에 있던 구슬을 오른쪽으로 한 칸 이동
            if red[1] > blue[1]:
                ry+=1
            elif red[1] < blue[1]:
                by+=1
                
    elif direction == 'right':
        while (by < M-1):
            if maze[bx][by+1] == 'O':
                return # 파란 구슬이 들어가 실패
            elif maze[bx][by+1] == '#':
                break
            by+=1
        
        while (ry < M-1):
            if maze[rx][ry+1] == 'O':
                ans = min(ans, cnt)
                return # 성공
            elif maze[rx][ry+1] == '#':
                break
            ry+=1
        
        if (rx, ry) == (bx, by): #구슬이 붙어있는 경우
            # 본래 왼쪽에 있던 구슬을 왼쪽으로 한 칸 이동
            if red[1] < blue[1]:
                ry-=1
            elif red[1] > blue[1]:
                by-=1

    if red == [rx, ry] and blue == [bx, by]:
        return 11;
    
    for direction in ('up', 'down', 'left', 'right'):
        move([rx, ry], [bx, by], direction, cnt+1)

ans = 100
for direction in ('up', 'down', 'left', 'right'):
    move(red, blue, direction, 1)

if ans == 100:
    print(-1)
else:
    print(ans)
