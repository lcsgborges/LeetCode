class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        i = 0
        if len(word1) > len(word2):
            tam = len(word1)
        else:
            tam = len(word2)

        while (i < tam):
            if (i < len(word1)):
                new_word+=word1[i]
            if (i < len(word2)):
                new_word+=word2[i]
            i+=1
        return new_word

solution = Solution()
print(solution.mergeAlternately("lucas", "borges"))
