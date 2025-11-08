# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         temp = "".join(c for c in s.lower() if c.isalnum())
#         print(temp)
#         return temp == temp[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l, r = l + 1, r - 1
        return True

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution().isPalindrome(s)
    print(sol)
    s = "0P"
    sol = Solution().isPalindrome(s)
    print(sol)