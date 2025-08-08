def printReverse(msg, len):
    stack = []
    for i in msg:
        stack.append(i)
    stack.reverse()
    result = ""
    for j in stack:
        result += j
    print(result)
instr = "자료구조"
printReverse(instr, len(instr))