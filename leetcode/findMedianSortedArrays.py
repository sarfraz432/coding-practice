class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        
if __name__ == "__main__":
    nums1 = [1, 3, 3, 5]
    nums2 = [2, 9]
    sol = Solution().findMedianSortedArrays(nums1=nums1, nums2=nums2)
    print(sol)