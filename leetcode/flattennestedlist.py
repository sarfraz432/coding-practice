
from typing import List
class Solution:
    def FlattenNestedList(self, list1: List) -> List:
        out_list = []
        def fun(list1):
            for item in list1:
                if isinstance(item, list):
                    fun(list1=item)
                else:
                    out_list.append(item)
        fun(list1)
        return out_list
        
if __name__ == "__main__":
    list1 = [[[[[[42]]]]]]
    sol = Solution().FlattenNestedList(list1=list1)
    print(sol)