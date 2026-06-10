class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None


node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)
node4 = LinkedList(4)
node5 = LinkedList(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

currentNode = node1
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.next
print("Null")