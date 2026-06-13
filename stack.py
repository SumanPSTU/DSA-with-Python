class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__count = 0
        self.__back = None
        self.__front = None
    def push(self,data):
        new_node = Node(data)
        if self.__count ==0:
            self.__front = self.__back = new_node
            self.__count +=1
            return
        else:
            new_node.next = self.__front
            self.__front = new_node
            self.__count +=1
            return

    def pop(self):
        if self.__count == 0:
            print("The stack is empty")
            return
        self.__front = self.__front.next
        self.__count -=1
        return
    def display(self):
        if self.__count ==0:
            print("The stack is Null")
            return
        __current = self.__front
        while __current:
            print(__current.data,end="->")
            __current = __current.next
        print("Null")
        return
    def get_size(self):
        print(self.__count)
    def get_front(self):
        print(self.__front.data)
    def get_back(self):
        print(self.__back.data)

stack = Stack()
stack.display()
stack.push(20)
stack.push(30)
stack.push(10)
stack.push(40)
stack.push(70)
stack.display()
stack.get_front()
stack.get_back()
stack.get_size()
