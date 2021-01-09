class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        # 应该是回溯算法 + 贪心思想
        # 但是贪心应该是按 position 而不是按 number
        
        res = [0 for _ in range(2*n - 1)]
        successFlag = []
        notUsed = range(1, n+1)
        
        def backtrack(pos):
            ##print pos
            ##print res
            ##print notUsed
            for num in sorted(notUsed, reverse=True):
                if num == 1:
                    res[pos] = 1
                    notUsed.remove(1)
                    if notUsed == []:
                        successFlag.append(1)
                        return
                    nextPos = res.index(0)
                    backtrack(nextPos)
                    if successFlag:
                        return
                    res[pos] = 0
                    notUsed.append(1)
                if pos + num < 2*n - 1 and res[pos] == 0 and res[pos + num] == 0:
                    res[pos] = res[pos+num] = num
                    notUsed.remove(num)
                    if notUsed == []:
                        successFlag.append(1)
                        return
                    nextPos = res.index(0)
                    ##print res
                    ##print notUsed
                    backtrack(nextPos)
                    if successFlag:
                        return
                    res[pos] = res[pos+num] = 0
                    notUsed.append(num)
        
        backtrack(0)
        return res
    
"""
https://leetcode-cn.com/submissions/detail/137249138/

20 / 20 个通过测试用例
状态：通过
执行用时: 60 ms
内存消耗: 12.8 MB
"""
