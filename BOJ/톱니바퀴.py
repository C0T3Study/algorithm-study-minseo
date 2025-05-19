import sys
input = sys.stdin.readline

first = input()
second = input()
third = input()
fourth = input()
index = [-1, 0, 0, 0, 0]

K = int(input())

def lotate(already, wheel, direction):
    temp_index = index[wheel]
    
    if direction == 1:
        index[wheel] = (index[wheel]-1)%8
    else:
        index[wheel] = (index[wheel]+1)%8
        
    if wheel == 1:
        if already != 2 and first[(temp_index+2)%8] != second[(index[2]+6)%8]:
            lotate(wheel, 2, -direction)
    
    elif wheel == 2:
        if already != 1 and first[(index[1]+2)%8] != second[(temp_index+6)%8]:
            lotate(wheel, 1, -direction)
        if already != 3 and second[(temp_index+2)%8] != third[(index[3]+6)%8]:
            lotate(wheel, 3, -direction)
    
    elif wheel == 3:
        if already != 2 and second[(index[2]+2)%8] != third[(temp_index+6)%8]:
            lotate(wheel, 2, -direction)
        if already != 4 and third[(temp_index+2)%8] != fourth[(index[4]+6)%8]:
            lotate(wheel, 4, -direction)
    
    elif wheel == 4:
        if already != 3 and third[(index[3]+2)%8] != fourth[(temp_index+6)%8]:
            lotate(wheel, 3, -direction)

for _ in range(K):
    wheel, direction = map(int, input().split())
    lotate(-1, wheel, direction)

ans = int(first[index[1]])*1 + int(second[index[2]])*2 + int(third[index[3]])*4 + int(fourth[index[4]])*8
print(ans)
