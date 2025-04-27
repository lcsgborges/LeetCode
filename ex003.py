class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        while (i < len(nums)):
            j = i + 1
            while (j< len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j+=1
            i+=1
        return []

solution = Solution()
print(solution.twoSum([3,3], 3))

# time complexity -> O(n^2)
# space complexity -> O(1)