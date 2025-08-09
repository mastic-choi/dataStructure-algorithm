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

class CirCularDeque(myQueue):
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    #연산이 동일한 함수 호출
    def addRear(self, item): self.Enque(item)
    def deleteFront(self): return self.deque()#준말로 Deque를 쓴건데 이게 덱(Deque)랑 겹칠줄 몰랐음
    def getFront(self): return self.peek()

    #새로 구현해야하는 함수들 생성
    def addFront(self, e):
        #Queue의 맨 앞에 item 추가
        if not self.isFull():
            self.myArray[self.front] = e
            self.front = (self.front-1+self.capacity)%self.capacity
        else: pass
    def deleteRear(self):
        #Queue의 맨 뒤에서 item 삭제
        if not self.isEmpty():
            item = self.myArray[self.rear]
            self.rear = (self.rear-1+self.capacity)%self.capacity
            return item
        else:
            pass
    def getRear(self):
        #Queue의 맨 뒤의 값 호출
        if not self.isEmpty():
            return self.myArray[self.rear]
        else: pass


dq = CirCularDeque()
for i in range(9):
    if i%2==0: dq.addRear(i)
    else: dq.addFront(i)
dq.display("홀수는 전단, 짝수는 후단 삽입 ")

for i in range(2): dq.deleteFront()
for i in range(3): dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9,14): dq.addFront(i)
dq.display("전단에 9~13 삽입")