N = int(input())
seq = list(map(int, input().split()))
operators = list(map(int, input().split()))

plus = operators[0]
minus = operators[1]
mult = operators[2]
div = operators[3]
maximum = -10e10
minimum = 10e10

def caculate():
    global maximum, minimum
    i = 0
    current = seq[i]
    for operation in location:
        i+=1
        if operation == '+':
            current = current + seq[i]
        elif operation == '-':
            current = current - seq[i]
        elif operation == '*':
            current = current * seq[i]
        elif operation == '//':
            if current < 0:
                current = -(-current//seq[i])
            else:
                current = current // seq[i]
    maximum = max(maximum, current)
    minimum = min(minimum, current)


def locate_div(index, cnt):
    while True:
        if cnt == div:
            caculate()
            return
        if index >= N-1:
            return
        if location[index] == '':
            location[index] = '//'
            locate_div(index+1, cnt+1)
            location[index] = ''
        index+=1

def locate_mult(index, cnt):
    while True:
        if cnt == mult:
            locate_div(0, 0)
            return
        if index >= N-1:
            return
        if location[index] == '':
            location[index] = '*'
            locate_mult(index+1, cnt+1)
            location[index] = ''
        index+=1

def locate_minus(index, cnt):
    while True:
        if cnt == minus:
            locate_mult(0, 0)
            return
        if index >= N-1:
            return
        if location[index] == '':
            location[index] = '-'
            locate_minus(index+1, cnt+1)
            location[index] = ''
        index+=1

def locate_plus(index, cnt):
    while True:
        if cnt == plus:
            locate_minus(0, 0)
            return
        if index >= N-1:
            return
        if location[index] == '':
            location[index] = '+'
            locate_plus(index+1, cnt+1)
            location[index] = ''
        index+=1

location = ['']*(N-1)
locate_plus(0, 0)
print(maximum)
print(minimum)
