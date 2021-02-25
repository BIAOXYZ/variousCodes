class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """

        # plain的哈希表/集合法，应该会超时。。。不然不像hard。

        newWords = [set(word) for word in words]
        newPuzzles = [[puzzle[0], set(puzzle)] for puzzle in puzzles]
        
        answer = []
        for i, newPuzzle in enumerate(newPuzzles):
            num = 0
            for newWord in newWords:
                if newPuzzle[0] in newWord and newWord.issubset(newPuzzle[1]):
                    num += 1
            answer.append(num)
        return answer
        
"""
https://leetcode-cn.com/submissions/detail/148785876/

9 / 10 个通过测试用例
状态：超出时间限制
"""
