# 2239. Find Closest Number to Zero
# Given an integer array nums of size n, return the number with the value closest to 0 in nums.
# If there are multiple answers, return the number with the largest value.
from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for n in nums:
            if abs(n) < abs(closest):
                closest = n
            if abs(n) == abs(closest) and n > closest:
                closest = n
        return closest
        

if __name__ == "__main__":
    nums =[2,-1,1]
    sol = Solution().findClosestNumber(nums)
    print(sol)