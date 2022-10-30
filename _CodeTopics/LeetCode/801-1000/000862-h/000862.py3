class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        # 主要参考了这个：
        # https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/liang-zhang-tu-miao-dong-dan-diao-dui-li-9fvh/

        n = len(nums)
        res = n + 1
        prefixSum = list(accumulate(nums, initial=0))
        ## print(prefixSum)
        dqIndex = deque()

        for i in range(n+1):  # 前缀和数组用的是带 0 型的，所以长度是 n+1。
            currPrefixSum = prefixSum[i]
            while dqIndex and currPrefixSum - prefixSum[dqIndex[0]] >= k:
                res = min(res, i - dqIndex[0])
                dqIndex.popleft()
            while dqIndex and currPrefixSum <= prefixSum[dqIndex[-1]]:
                dqIndex.pop()
            dqIndex.append(i)
        return res if res != n + 1 else -1
        
"""
https://leetcode.cn/submissions/detail/377911405/

执行用时：
320 ms
, 在所有 Python3 提交中击败了
94.95%
的用户
内存消耗：
25.6 MB
, 在所有 Python3 提交中击败了
93.57%
的用户
通过测试用例：
97 / 97
"""
