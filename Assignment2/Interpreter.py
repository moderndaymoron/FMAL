import sys

identifiers = {}
stack = []
def main():
    inp = sys.stdin
    for line in inp:
        handler(line)
def handler(line):
    first = ""
    second = ""
    if line[:4] == 'PUSH':
        element = line[5:-1]
        if element in identifiers:
            stack.append(identifiers[element])
        else:
            stack.append(element)
    elif line[:6] == 'ASSIGN':
        checkError('ASSIGN')
        first = popper()
        second = popper()
        identifiers[second] = first
        sys.stdout.write(str(second) + " = " + str(first) + ';\n')
    elif line[:3] == 'ADD':
        checkError('ADD')
        first = popper()
        second = popper()
        stack.append(first + second)
    elif line[:3] == 'SUB':
        checkError('SUB')
        first = popper()
        second = popper()
        stack.append(second - first)
    elif line[:4] == 'MULT':
        checkError('MULT')
        first = popper()
        second = popper()
        stack.append(first * second)
    elif line[:5] == 'PRINT':
        if len(stack) < 1:
            sys.stdout.write("Error for operator PRINT\n")
        sys.stdout.write(str(stack[-1]) + '\n')

def popper():
    last = str(stack[-1])
    if last.isdigit():
        return int(stack.pop())
    else:
        if last in identifiers:
            stack.pop()
            return identifiers[last]
        else:
            return stack.pop()
def checkError(operator):
    if len(stack) < 2:
        sys.stdout.write("Error for operator: " + operator + '\n')
        sys.exit()

if __name__ == "__main__": main()