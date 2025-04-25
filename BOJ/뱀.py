import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

apples = [[False]*(N+1) for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    apples[x][y] = True
    
L = int(input())

turn = []
for _ in range(L):
    X, C = input().split()
    turn.append((int(X), C))
    
def turn_right(current):
    if current == 'up':
        return 'right'
    elif current == 'down':
        return 'left'
    elif current == 'left':
        return 'up'
    elif current == 'right':
        return 'down'
    
def turn_left(current):
    if current == 'up':
        return 'left'
    elif current == 'down':
        return 'right'
    elif current == 'left':
        return 'down'
    elif current == 'right':
        return 'up'
    
time = 0
direction = 'right'
snake = [(1, 1)]
x, y = 1, 1
while True:
    time+=1

    # 진행
    if direction == 'up':
        x-=1
    elif direction == 'down':
        x+=1
    elif direction == 'left':
        y-=1
    elif direction == 'right':
        y+=1
    
    # 벽 혹은 자기 자신에 부딪혔는지
    if not (1<=x<=N and 1<=y<=N) or (x, y) in snake:
        break

    # 현재 칸 추가
    snake.append((x, y))
    # 사과가 없으면 꼬리 칸을 제거
    if not apples[x][y]:
        snake.pop(0)
    apples[x][y] = False
    
    # 방향 전환
    if turn and turn[0][0] == time:
        rotation = turn[0][1]
        turn.pop(0)
        if rotation == 'D':
            direction = turn_right(direction)
        elif rotation == 'L':
            direction = turn_left(direction)
    
print(time)
