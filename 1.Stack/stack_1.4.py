#스택의 응용: 괄호 검사
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

#입력된 문자가 괄호인지 아닌지 판단
def isBracket(x):
    if x in ['(',')','{','}','[',']']:
        return True
    else:
        return False

def checkBrackets(msg):
    lgt = len(msg)
    myStack = ArrayStack(lgt)

    for i in msg:
        if i in ['(','[','{']:
            myStack.push(i)
        elif i in [')',']','}']:
            if myStack.isEmpty():
                return False
            else :
                x = myStack.pop()
                if ( i == '(') and (x != ')') or ( i == '{') and (x != '}') or ( i == '[') and (x != ']'):
                    return False
    return myStack.isEmpty()

msg = str(input())
check = checkBrackets(msg)
print(check)


