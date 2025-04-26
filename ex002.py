class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        i = 0
        j = 0
        length = len(flowerbed)

        while (i < length):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or flowerbed[i-1] == 0
                empty_right = (i == length-1) or flowerbed[i+1] == 0

                if empty_right and empty_left:
                    flowerbed[i] = 1
                    j+= 1
            i+=1
        if j >= n:
            return True
        return False
               
solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1))