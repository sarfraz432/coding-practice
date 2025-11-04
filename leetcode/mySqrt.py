# 69. Sqrt(x)
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 1:
            return 0
        low = 1
        high = x
        while low <= high:
            mid = low + (high - low) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                high = mid - 1
            elif mid < x // mid:
                low = mid + 1
        return high

if __name__ == "__main__":
    sol = Solution().mySqrt(9990)
    print(sol)