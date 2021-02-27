class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """

        # 位运算 + 哈希表。难点就在于枚举每个puzzle的所有可能子集。

        freqWords = collections.Counter([])
        for word in words:
            bitMask = 0
            for ch in word:
                bitMask |= (1 << ord(ch) - ord("a"))
            if str(bin(bitMask)).count("1") <= 7:
                freqWords[bitMask] += 1

        answer = []
        for puzzle in puzzles:
            numOfWords = 0
            mask = 0
            for i in range(1, 7):
                mask |= (1 << (ord(puzzle[i]) - ord("a")))
            
            # 位运算的方式枚举puzzle的非空子集。
            subset = mask
            while subset:
                s = subset | (1 << (ord(puzzle[0]) - ord("a")))
                if s in freqWords:
                    numOfWords += freqWords[s]
                subset = (subset - 1) & mask
            
            # 前面的枚举方法会漏掉空集，这里补一下。
            if (1 << (ord(puzzle[0]) - ord("a"))) in freqWords:
                numOfWords += freqWords[1 << (ord(puzzle[0]) - ord("a"))]
            answer.append(numOfWords)
        return answer
        
"""
https://leetcode-cn.com/submissions/detail/149315474/

10 / 10 个通过测试用例
状态：通过
执行用时: 532 ms
内存消耗: 32.6 MB

执行用时：532 ms, 在所有 Python 提交中击败了79.08%的用户
内存消耗：32.6 MB, 在所有 Python 提交中击败了35.29%的用户
"""
