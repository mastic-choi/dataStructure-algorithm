#최선,최악,평균적인 호율성

def find_max(A:list):
    #시간복잡도(big-O) O(n)
    n = len(A)              #1번 연산
    max = A[0]              #1번 연산
    for i in range(n):      #n번 연산
        if A[i] > max :     #1번 연산
            max = A[i]      #1번 연산
    return max              

def find_key(A:list, key):
    #시간복잡도(big-O) O(n)
    n = len(A)          #1번 연산
    for i in range(A):
        if A[i] == key: #(최악) n번 반복, (최선) 1번 연산, (평균) (n+1)/2번 반복
            return i
    return -1