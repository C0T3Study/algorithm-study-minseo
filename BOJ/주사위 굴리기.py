import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

commands = list(map(int, input().split()))

dice = [-1, 0, 0, 0, 0, 0, 0]

for command in commands:
    
    # 이동&회전
    if command == 1: #동
        if y+1>M-1:
            continue
        y+=1
        dice[4], dice[1], dice[6], dice[3] = dice[1], dice[3], dice[4], dice[6]
        
    elif command == 2: #서
        if y-1<0:
            continue
        y-=1
        dice[3], dice[6], dice[1], dice[4] = dice[1], dice[3], dice[4], dice[6]
        
    elif command == 3: #북
        if x-1<0:
            continue
        x-=1        
        dice[5], dice[1], dice[6], dice[2] = dice[1], dice[2], dice[5], dice[6] 

    elif command == 4: #남
        if x+1>N-1:
            continue
        x+=1
        dice[2], dice[6], dice[1], dice[5] = dice[1], dice[2], dice[5], dice[6]
    
    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0
    
    print(dice[1])
