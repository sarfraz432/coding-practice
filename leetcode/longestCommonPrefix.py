# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix



if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    sol = Solution().longestCommonPrefix(strs)
    print(sol)