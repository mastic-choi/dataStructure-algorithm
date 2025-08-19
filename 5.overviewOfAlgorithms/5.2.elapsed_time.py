#실행 시간 측정방법
import time as t
def testAlgorithm(A = 0, B = 0, C = 0):
    max = A
    if B > max:
        max = B
    if C > max:
        max = C
    return max
a = input("숫자 입력하세요 : ")
b = input("숫자 입력하세요 : ")
c = input("숫자 입력하세요 : ")
start = t.time()
testAlgorithm(a, b, c)
end = t.time()
print("실행시간 = %.10f" %(end-start))

'''
해당 방법으로 알고리즘의 성능을 비교하는데 치명적인 약점이 있습니다.
1. 알고리즘을 반드시 '구현'해야 합니다.
2. 반드시 같은 조건의 하드웨어를 사용해야 합니다.
3. 프로그램 언어나 OS같은 소프트웨어 환경도 같아야 합니다.
4. 실험되지 않은 입력에 대해서는 실행 시간을 주장하기 어렵습니다.
'''