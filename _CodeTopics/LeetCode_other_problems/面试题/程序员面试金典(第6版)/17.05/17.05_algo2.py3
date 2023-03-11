class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:

        n = len(array)
        newArray = [1 if array[i].isalpha() else -1 for i in range(n)]
        prefixSum = list(accumulate(newArray))
        # print(newArray, prefixSum)

        ddic = defaultdict(list)
        for i in range(n):
            ddic[prefixSum[i]].append(i)
        # print(ddic)

        maxLen, startInd = 0, n+1
        for k, indices in ddic.items():
            if k == 0:
                currMaxLen = indices[-1] - 0 + 1
                currStartInd = 0
                if currMaxLen >= maxLen:
                    maxLen = currMaxLen
                    startInd = currStartInd
            else:
                if len(indices) >= 2:
                    currMaxLen = indices[-1] - indices[0]
                    currStartInd = indices[0] + 1
                    if currMaxLen > maxLen or (currMaxLen == maxLen and currStartInd < startInd):
                        maxLen = currMaxLen
                        startInd = currStartInd
        if startInd == n+1:
            return []
        return array[startInd : startInd + maxLen]
        
"""
https://leetcode.cn/submissions/detail/412027213/

执行用时：
116 ms
, 在所有 Python3 提交中击败了
95.79%
的用户
内存消耗：
37.7 MB
, 在所有 Python3 提交中击败了
5.27%
的用户
通过测试用例：
45 / 45
"""
