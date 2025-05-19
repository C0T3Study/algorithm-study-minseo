import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

lad =[[False for _ in range(N+1)] for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    
    lad[a][b] = True

def check():
    for n in range(1, N+1):
        cur = n
        for h in range(1, H+1):
            if lad[h][cur]:
                cur+=1
            elif lad[h][cur-1]:
                cur-=1

        if cur != n:
            return False
        
    return True


def func(n, h, cnt):
    global checked, ans
    
    if cnt == 4:
        return
    else:
        checked = check()
        if checked:
            ans = min(ans, cnt)
            return

    while True:
        if n == N:
            if h == H:
                break
            else:
                h+=1
                n=1
        else:
            n+=1
        
        if n<=N-1 and not lad[h][n]:
            if not lad[h][n-1] and not lad[h][n+1]:
                lad[h][n] = True
                func(n, h, cnt+1)
                lad[h][n] = False
            
checked = False
ans = 4
func(0, 1, 0)

if ans == 4:
    print(-1)
else:
    print(ans)
