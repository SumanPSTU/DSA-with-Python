class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Circuler_linked_list:
    def __init__(self):
        self.__head = self.__tail = None
        self.__count = 0
    def insert(self,data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
            self.__tail.next = self.__head
        self.__count +=1
        return
    def display(self):
        if self.__head is None:
            print("Null")
            return
        __current = self.__head
        for i in range(self.__count):
            print(__current.data,end="->")
            __current = __current.next
        print("Null")

    def get_size(self):
        print(self.__count)
    def get_head(self):
        print(self.__head.data)
    def get_tail(self):
        print(self.__tail.data)

circle = Circuler_linked_list()
circle.insert(3)
circle.insert(5)
circle.insert(2)
circle.insert(1)
circle.insert(30)
circle.get_size()
circle.get_head()
circle.get_tail()
circle.display()
