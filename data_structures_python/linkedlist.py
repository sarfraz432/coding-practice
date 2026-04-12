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

    def prependNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self, key):
        current = self.head
        # Case 1: The node to delete is the head
        if current and current.data == key:
            self.head = current.next
            return

        # Case 2: Search the rest of the list
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If current is None, we didn't find the key
        if current is None:
            return

        # If we reached here, current is the node to delete, and prev is the node before it
        if prev:
            prev.next = current.next

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

    print("Initial List (10 followed by 0 through 9):")
    ll.print()
