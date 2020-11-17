class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        # 用内置的map()加lambda来代替列表推导式。
        subtraction = map(lambda x, y : x-y, gas, cost)
        if sum(subtraction) < 0:
            return -1

        length = len(subtraction)
        skip_pos = 0
        for i in range(length):
            # 加这个skip_pos，就体现了答案里优化的部分了。也体现了为啥这题有点脑筋急转弯的意思。
            if i < skip_pos:
                continue
            addition = subtraction[i]
            j = i + 1
            while addition >= 0 and j % length != i:
                addition += subtraction[j%length]
                j += 1
            if addition < 0:
                skip_pos = j
                continue
            if j % length == i:
                return i
        return -1
        
"""
https://leetcode-cn.com/submissions/detail/124245255/

31 / 31 个通过测试用例
状态：通过
执行用时: 20 ms
内存消耗: 14.1 MB

执行用时：20 ms, 在所有 Python 提交中击败了81.59%的用户
内存消耗：14.1 MB, 在所有 Python 提交中击败了11.18%的用户
"""
