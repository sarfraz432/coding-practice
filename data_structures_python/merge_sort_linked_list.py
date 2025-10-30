import random
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
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    def findMiddleNode(self):
        if self.head != None:
            slow = self.head
            fast = self.head

            while fast != None:
                slow = slow.next
                fast = fast.next
                if fast:
                    fast = fast.next
            return slow
        return None
    def merge_sort(self):
        if list1 != None:
            # find middle node to split in half
            middle = self.findMiddleNode()
            if middle:
                print(middle.data)

if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()
    
    for i in range(0, 3):
        list1.addNode(random.randint(0, 100))
    for i in range(0, random.randint(1, 20)):
        list2.addNode(random.randint(0, 100))


    print("list1")
    list1.print()
    list1.merge_sort()
    # print("list2")
    # list2.print()