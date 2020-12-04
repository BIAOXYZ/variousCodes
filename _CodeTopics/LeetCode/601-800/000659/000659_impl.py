from collections import defaultdict
import heapq
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        defaultDic = defaultdict(list)
        for num in nums:
            hp = defaultDic.get(num - 1)
            # 这里要是用下面这句是不对的！因为如果 hp 是个空list的话，用下面这句会进到if分支。
            # （因为 [] 确实不等于 None）。但是其实 hp 是空list的时候我们希望进入else分支。
            # if hp != None:
            if hp:
                shortestLength = heapq.heappop(hp)
                heapq.heappush(defaultDic[num], shortestLength + 1)
            else:
                heapq.heappush(defaultDic[num], 1)
        
        return not any(hp and hp[0] < 3 for hp in defaultDic.values())
        
"""
https://leetcode-cn.com/submissions/detail/128716233/

180 / 180 个通过测试用例
状态：通过
执行用时: 468 ms
内存消耗: 14.2 MB

执行用时：468 ms, 在所有 Python 提交中击败了57.69%的用户
内存消耗：14.2 MB, 在所有 Python 提交中击败了16.00%的用户
"""
