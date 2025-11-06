# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from itertools import zip_longest
from typing import Optional
class Solution:
    def addTwoNumbers(self, l1, l2):
        sum = []
        carry = 0
        for a,b in zip_longest(l1, l2, fillvalue=0):
            digit = a + b + carry if a + b + carry < 10 else (a + b + carry) - 10
            carry = 1 if a + b + carry >= 10 else 0
            # print(digit)
            sum.append(digit)
        if carry:
            sum.append(1)
        return sum


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        temp1 = l1
        temp2 = l2
        sum_list = ListNode()
        temp_sum = sum_list
        while temp1 and temp2:
            digit = (
                temp1.val + temp2.val + carry
                if temp1.val + temp2.val + carry < 10
                else temp1.val + temp2.val + carry - 10
            )
            carry = 1 if temp1.val + temp2.val + carry >= 10 else 0
            temp_sum.next = ListNode(digit)
            temp1 = temp1.next
            temp2 = temp2.next
            temp_sum = temp_sum.next
        for list in [temp1, temp2]:
            if list:
                while list:
                    digit = (
                        list.val + carry
                        if list.val  + carry < 10
                        else list.val  + carry - 10
                    )
                    carry = 1 if list.val + carry >= 10 else 0
                    temp_sum.next = ListNode(digit)

                    list = list.next
                    temp_sum = temp_sum.next
        if carry:
            temp_sum.next = ListNode(carry)
        return sum_list.next


if __name__ == "__main__":
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    sol = Solution().addTwoNumbers(l1, l2)
    print(sol)