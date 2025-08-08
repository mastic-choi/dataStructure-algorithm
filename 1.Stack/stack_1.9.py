#하노이의 탑 몇 번 옮겨야 하는지 연산
def hanoi(x):
    if x == 1:
        return 1
    elif x > 1:
        return hanoi(x-1)*2 + 1
#하노이의 탑 이동 경로
def hanoi_tower(n, fr, tmp, to):
    if n==1:
        print("원판 1: %s --> %s" %(fr, to))
    else :
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)
print(hanoi(3))
print(hanoi_tower(4, 'A', 'B', 'C'))