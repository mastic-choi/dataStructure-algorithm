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

    def Enque2(self, itm): #링버퍼 추가
        self.rear = (self.rear+1)%self.capacity
        self.myArray[self.rear] = itm
        if self.isEmpty():
            self.front = (self.front+1)%self.capacity
        
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
q.display("초기 상태")
for i in range(6):
    q.Enque2(i)
q.display("삽입 0-5")
q.Enque2(7)
q.Enque2(8)

q.display("삽입 7,8")
q.deque(); q.deque()
q.display("삭제 실행 후")