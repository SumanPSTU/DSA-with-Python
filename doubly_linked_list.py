class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.priv = None

class doubly_linked_list:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def insert(self,data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node

        else:
            new_node.priv = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
        self.__count +=1
        return
    def display(self):
        if self.__head is None:
            print("Null")
        __current = self.__head
        while __current:
            print(__current.data,end="<->")
            __current = __current.next
        print("Null")

    def get_size(self):
        print(self.__count)
    def get_head(self):
        print(self.__head.data)
    def get_tail(self):
        print(self.__tail.data)


list = doubly_linked_list()
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(30)
list.insert(40)
list.insert(45)
list.display()
list.get_size()
list.get_head()
list.get_tail()