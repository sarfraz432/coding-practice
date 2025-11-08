class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([sub for sub in s.split(" ") if sub][-1])
        

if __name__ == "__main__":
    s = "   fly me   to   the moon  "
    sol = Solution().lengthOfLastWord(s)
    print(sol)