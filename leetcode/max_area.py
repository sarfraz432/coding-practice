from typing import List
# Brute force solution
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         max_area = 0
#         for i in range(0, len(height) - 1):
#             for j in range(i + 1, len(height)):
#                 distance = (j - i)
#                 minimum = (min(height[i], height[j]))
#                 area = distance * minimum
#                 if area > max_area:
#                     max_area = area
#         return max_area 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            distance = (end - start)
            min_height = min(height[start], height[end])
            area = min_height * distance
            if area > max_area:
                max_area = area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area 

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    # height = [1,1]
    sol = Solution().maxArea(height)
    print(sol)