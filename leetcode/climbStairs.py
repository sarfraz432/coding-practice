class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def fun(m):
            if m <= 2:
                return m
            if m in mem:
                return mem[m]
            else:
                mem[m] = fun(m - 1) + fun(m - 2)
                return mem[m]
        return fun(n)
    


if __name__ == "__main__":
    sol = Solution().climbStairs(3)
    print(sol)