import sys
input = sys.stdin.readline

N, L = map(int, input().split())

roads = []

for _ in range(N):
    roads.append(list(map(int, input().split())))

def check_road(road):
    global ans
    already = [False for _ in range(N)]
    for n in range(N-1):
        # if flat
        if road[n] == road[n+1]:
            continue
        if abs(road[n] - road[n+1]) == 1:
            # up
            if road[n]+1 == road[n+1]:
                for k in range(n, n-L, -1):
                    # if can not put ramp
                    if k<0 or already[k] or road[k] != road[n]:
                        return
                # if can put ramp
                already[n] = True          
            # down
            else:
                for k in range(n+1, n+1+L, 1):
                    # if can not put ramp
                    if k>N-1:
                        return
                    if already[k]:
                        return 
                    if road[k] != road[n+1]:
                        return
                # if can put ramp
                already[n+L] = True            
        else:
            return
    ans+=1
    
ans = 0
for n in range(N):
    # check row
    check_road(roads[n])
    # check column
    check_road([roads[m][n] for m in range(N)])

print(ans)
