class Solution:
    def reverse(self, x: int) -> int:
        
        if x < 0:
            x:list = list(str(x))
            del x[0]
            string = ''
            for num in reversed(x):
                string += num
            x = int('-' + string)
        else:
            x = str(x)
            x = x[::-1]
            x = int(x)
        
        if x > 2**31 -1 or x < -2**31:
            return 0

        return x

solution = Solution()
print(solution.reverse(-136469))
