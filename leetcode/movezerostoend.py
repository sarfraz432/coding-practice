# 27. Remove Element

# move all zeros to end and return non zero list

from typing import List
class Solution:
    def removeNonZero(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return j


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    sol = Solution().removeNonZero(nums)
    print(sol, nums[:sol])
