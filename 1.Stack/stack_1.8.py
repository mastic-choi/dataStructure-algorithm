#순환 구조로 팩토리얼 구현하기
def factorial(n):
    if n == 1:
        return 1
    elif n > 1:
        return factorial(n-1)*n
    else:
        pass
