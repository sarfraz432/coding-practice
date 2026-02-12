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
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def split_in_half(self, head):
        """Split list starting at `head` into two halves.
        Returns (left_head, right_head).
        """
        if not head or not head.next:
            return head, None
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # slow is start of right half; cut the list
        prev.next = None
        left = head
        right = slow
        return left, right
    def _merge_sorted(self, l1, l2):
        dummy = Node(0)
        tail = dummy
        a, b = l1, l2
        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a if a else b
        return dummy.next
    def _merge_sort(self, head):
        if not head or not head.next:
            return head
        left, right = self.split_in_half(head)
        left_sorted = self._merge_sort(left)
        right_sorted = self._merge_sort(right)
        return self._merge_sorted(left_sorted, right_sorted)
    def merge_sort(self):
        # Sort the linked list in-place and update `self.head`.
        self.head = self._merge_sort(self.head)

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