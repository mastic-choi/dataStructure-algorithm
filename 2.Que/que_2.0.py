#P79 5번 Queue로 피보나치 수열 구현하기
# 1. 처음음 Queue에는 fibo(0), fibo(1)의 값을 구한다.
# 2. fibo(2) = fibo(0) + fibo(1)이고 fibo(3) = fibo(2) + fibo(1), 
# 즉 Queue의 형식으로 선입 선출로 규안에 2개만 남겨두고 남은 아이템의 합이 다음 피보나치 수열의 값이다.
import collections
def fibonacci(n):
    q = collections.deque()
    q.append(0)
    q.append(1)
    for i in range(2, n+1):
        a, b = q.popleft(), q.popleft()
        q.append(b); q.append(a+b)
    a, b = q.popleft(), q.popleft()
    return a + b
print(fibonacci(9))