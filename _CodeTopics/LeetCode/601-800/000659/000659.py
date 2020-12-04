import heapq
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 和答案（哈希表 + 最小堆）思想类似，只不过没有用collections里的defaultdict
        # 一会可能考虑再写一个用defaultdict的版本？

        dic = {}
        for num in nums:
            if dic.has_key(num-1):
                currHeap = dic[num-1]
                shortestLen = heapq.heappop(currHeap)
                # 这个if分支是为了防止剩下个空集导致下一轮还是同样的num时会报错。
                # 比如[1,2,3,3,4,5]，第二个3来时，如果还有个 dic[2] = [] 在字典里会有问题。
                if dic[num-1] == []:
                    del dic[num-1]
                if dic.has_key(num):
                    heapq.heappush(dic[num], shortestLen+1)
                else:
                    dic[num] = [shortestLen+1]
                    heapq.heapify(dic[num])
            else:
                if dic.has_key(num):
                    heapq.heappush(dic[num], 1)
                else:
                    dic[num] = [1]
                    heapq.heapify(dic[num])

        for hp in dic.values():
            if hp and hp[0] < 3:
                return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/128704674/

180 / 180 个通过测试用例
状态：通过
执行用时: 432 ms
内存消耗: 14 MB

执行用时：432 ms, 在所有 Python 提交中击败了57.69%的用户
内存消耗：14 MB, 在所有 Python 提交中击败了38.00%的用户
"""
