#스택으로 PS하기
'''
스택을 이용해 말을 거꾸로 뒤집는 프로그램을 만들어봅시다. 
문자열을 입력받고, 입력된 문자들을 순서대로 스택에 모두 넣은 다음
하나씩 꺼내서 출력하기만 하면 됩니다.
'''

class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1

    def isEmpty(self):
        if self.top == -1 :
            return True
        else:
            return False

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else :
            print("Stack Overflow")
            exit()

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else :
            print("Stack underFlow")
            exit()

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

    def size(self):
        return self.top+1
    
s = ArrayStack(100)

msg = input("문자열을 입력해주세요 : ")
for c in msg:
    s.push(c)

print("문자열 출력 : ", end='')
while not s.isEmpty():
    print(s.pop(), end='')
print()