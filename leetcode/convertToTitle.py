class Solution:
    # def convertToTitle(self, columnNumber: int) -> str:
    #     out = ""
    #     while columnNumber > 26:
    #         reminder = (columnNumber % 26) 
    #         out += chr(64+reminder)
    #         columnNumber = columnNumber // 26
    #     out += chr(64+columnNumber)
    #     return out[::-1]
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            columnNumber -= 1
            out += chr(65 + columnNumber % 26)
            columnNumber //= 26
        return out[::-1]


if __name__ == "__main__":
    columnNumber = 1
    res = Solution().convertToTitle(columnNumber)
    print(res)
