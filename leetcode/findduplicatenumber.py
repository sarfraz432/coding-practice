
from typing import List
class Solution:
    def find_duplicate_in_list(self, nums: List[int]) -> int:
        if len(nums) < 2:
            raise ValueError("Input list must contain at least 2 elements.")

        n = len(nums) - 1
        for value in nums:
            if value < 1 or value > n:
                raise ValueError(
                    f"Invalid value {value}. All values must be between 1 and {n}."
                )

        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return slow


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    sol = Solution().find_duplicate_in_list(nums=nums)
    print(sol)
