import sys


class MyStack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return -1
        return self.stack[-1]
    
    def is_empty(self):
        return int(len(self.stack) == 0)
    
    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    n = int(input())
    stack = MyStack()
    
    for _ in range(n):
        command = sys.stdin.readline().split()
        status = command[0]
        
        if status == "push":
            stack.push(command[1])
        elif status == "pop":
            print(stack.pop())
        elif status == "top":
            print(stack.top())
        elif status == "empty":
            print(stack.is_empty())
        elif status == "size":
            print(stack.size())
