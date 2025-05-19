N, M = map(int, input().split())

office = []
for _ in range(N):
    office.append(list(map(int, input().split())))
    
cctvs = []
for i in range(N):
    for j in range(M):
        if 1<=office[i][j]<=5:
            cctvs.append((office[i][j], i, j))

def monitor_up(x, y, office):
    _office = list(map(list, office))
    while (0<=x-1):
        x-=1
        if _office[x][y] == 6:
            break
        if _office[x][y] == 0:
            _office[x][y] = '#'
            
    return _office
    
def monitor_down(x, y, office):
    _office = list(map(list, office))
    while (x+1<=N-1):
        x+=1
        if _office[x][y] == 6:
            break
        if _office[x][y] == 0:
            _office[x][y] = '#'
    return _office

def monitor_left(x, y, office):
    _office = list(map(list, office))
    while (0<=y-1):
        y-=1
        if _office[x][y] == 6:
            break
        if _office[x][y] == 0:
            _office[x][y] = '#'
    return _office

def monitor_right(x, y, office):
    _office = list(map(list, office))
    while (y+1<=M-1):
        y+=1
        if _office[x][y] == 6:
            break
        if _office[x][y] == 0:
            _office[x][y] = '#'
    return _office


def monitor(index, office):
    global ans
    
    if index >= len(cctvs):
        cnt=0
        for i in range(N):
            for j in range(M):
                if office[i][j]==0:
                    cnt+=1
        ans = min(ans, cnt)
        return
    
    cctv = cctvs[index]
    num = cctv[0]
    x, y = cctv[1], cctv[2]
    
    if num == 1:
        _office = monitor_up(x, y, office)
        monitor(index+1, _office)
        
        _office = monitor_down(x, y, office)
        monitor(index+1, _office)
        
        _office = monitor_left(x, y, office)
        monitor(index+1, _office)
        
        _office = monitor_right(x, y, office)
        monitor(index+1, _office)
        
    elif num == 2:
        _office = monitor_up(x, y, office)
        _office = monitor_down(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_left(x, y, office)
        _office = monitor_right(x, y, _office)
        monitor(index+1, _office)
        
    elif num == 3:
        _office = monitor_up(x, y, office)
        _office = monitor_right(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_up(x, y, office)
        _office = monitor_left(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_left(x, y, office)
        _office = monitor_down(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_down(x, y, office)
        _office = monitor_right(x, y, _office)
        monitor(index+1, _office)
        
    elif num == 4:
        _office = monitor_left(x, y, office)
        _office = monitor_up(x, y, _office)
        _office = monitor_right(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_up(x, y, office)
        _office = monitor_right(x, y, _office)
        _office = monitor_down(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_left(x, y, office)
        _office = monitor_down(x, y, _office)
        _office = monitor_right(x, y, _office)
        monitor(index+1, _office)
        
        _office = monitor_up(x, y, office)
        _office = monitor_left(x, y, _office)
        _office = monitor_down(x, y, _office)
        monitor(index+1, _office)
        
    elif num == 5:
        _office = monitor_up(x, y, office)
        _office = monitor_right(x, y, _office)
        _office = monitor_down(x, y, _office)
        _office = monitor_left(x, y, _office)
        monitor(index+1, _office)
    
ans = 100
monitor(0, office)
print(ans)
