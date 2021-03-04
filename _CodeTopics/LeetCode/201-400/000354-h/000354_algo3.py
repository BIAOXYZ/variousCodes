class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # 同样参见LC300，这里对应的是`000300_algo2.py`。

        if not envelopes:
            return 0

        envelopes.sort(key = lambda x : (x[0], -x[1]))
        heightList = [envelope[1] for envelope in envelopes]
        length = len(envelopes)

        longestList = []
        for i in range(length):
            if not longestList or heightList[i] > longestList[-1]:
                longestList.append(heightList[i])
            else:
                left, right = 0, len(longestList) - 1
                index = right
                while left <= right:
                    mid = left + (right - left) / 2
                    if longestList[mid] > heightList[i]:
                        index = mid
                        right = mid - 1
                    elif longestList[mid] < heightList[i]:
                        left = mid + 1
                    else:
                        index = mid
                        break
                longestList[index] = heightList[i]
        return len(longestList)
        
"""
https://leetcode-cn.com/submissions/detail/151190740/

84 / 84 个通过测试用例
状态：通过
执行用时: 68 ms
内存消耗: 14.6 MB

执行用时：68 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：14.6 MB, 在所有 Python 提交中击败了100.00%的用户
"""
"""
我去，LeetCode做题过程中第一个双百出现了。。。
"""
