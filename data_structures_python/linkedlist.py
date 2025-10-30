
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.addNode(10)
    for i in range(0, 10):
        ll.addNode(i)


    ll.print()