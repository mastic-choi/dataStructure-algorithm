import random

class myQueue:
    def __init__(self, capacity=10):
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.myArray = [None]*self.capacity
    
    def isEmpty(self):
        if self.front == self.rear:
            return True
        else: return False
    '''
    원형 Queue가 Full인 상태에서는 front == rear만으로는 Queue의 공백상태를 확인하기 어려움.
    front가 rear바로 다음에 있으면 포화상태로 정의
    '''
    def isFull(self):
        if self.front == (self.rear+1)%self.capacity:
            return True
        else: return False
    
    def Enque(self, elmt):
        if self.isFull():
            return "OverFlow"
        else:
            self.rear = (self.rear+1)%self.capacity
            self.myArray[self.rear] = elmt

    def deque(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            self.front = (self.front+1)%self.capacity
            return self.myArray[self.front]
    def peek(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            return self.myArray[(self.front+1)%self.capacity]

    def size(self):
        return (self.rear-self.front+self.capacity)%self.capacity
    
    def display(self, msg):
        print(msg, end=": [")
        for i in range(self.front+1, self.front+1+self.size()):
            print(self.myArray[i%self.capacity], end =" ")
        print("]")
    
q = myQueue(8)
q.display("초기상태")
while not q.isFull():
    q.Enque(random.randint(0,100))
q.display("포화 상태")
print("삭제순서 : ",end = '')
