class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.__head = self.__tail = None
        self.__count = 0

    def insert(self,data):
        new_node = Node(data)
        new_node.next
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count +=1
        return
    def display(self):
        if self.__head is None:
            print("Null")

        current = self.__head
        while current:
            print(current.data,end="->")
            current = current.next
        print("Null")
        return
    def get_size(self):
        print(self.__count)
        return
    def get_head(self):
        print(self.__head.data)
        return
    def get_tail(self):
        print(self.__tail.data)
list = LinkedList()
list.insert(1)
list.insert(4)
list.insert(2)
list.insert(6)
list.insert(9)
list.get_size()
list.get_head()
list.get_tail()
list.display()

