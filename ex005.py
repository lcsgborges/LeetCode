class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        for i in range(0, len(sentence)):
            if sentence[i][0:len(searchWord)] == searchWord:
                return i + 1
            
        return -1


solution = Solution()
print(solution.isPrefixOfWord("i love eating burger", "burg"))