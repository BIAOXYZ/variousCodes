import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        # 比较流氓的方法：堆。每次pop出一个，肯定是当前最小，然后把每个素数都乘一下，在push进堆里。
        # 更具体的细节，参见官方答案吧。

        currNums = [1]
        alreadyInsert = set([1])

        heapq.heapify(currNums)
        while n > 0:
            n -= 1
            num = heapq.heappop(currNums)
            for prime in primes:
                if num * prime not in alreadyInsert:
                    heapq.heappush(currNums, num * prime)
                    alreadyInsert.add(num * prime)
        return num
        
"""
https://leetcode-cn.com/submissions/detail/205123375/

83 / 83 个通过测试用例
状态：通过
执行用时: 1708 ms
内存消耗: 96.6 MB

执行用时：1708 ms, 在所有 Python 提交中击败了34.52%的用户
内存消耗：96.6 MB, 在所有 Python 提交中击败了26.19%的用户
"""
