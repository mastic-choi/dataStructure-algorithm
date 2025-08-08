#P51 연습문제를 풀어보자
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
    #연습 문제 2번 : 스택을 공백 상태로 초기화하는 Clear 연산
    def clear(self):
        self.array = [None]*0
        self.top = -1
    
    def display(self):
        for i in self.array:
            if i != None:
                print(i)

n = ArrayStack(3)
n.push(1)
n.push(5)
n.display()