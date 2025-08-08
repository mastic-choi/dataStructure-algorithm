#파이썬에서 스택 사용하기
s = list()

msg = input("문자열을 입력하세요 : ")
for i in msg:
    s.append(i)

print("문자열 출력 : ", end = "")
while len(s) > 0:
    print(s.pop(), end ="")
print()