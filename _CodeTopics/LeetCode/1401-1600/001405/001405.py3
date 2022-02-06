import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        # 感觉题目里那句 “如果不存在这样的字符串 s ，请返回一个空字符串 ""。”
        # 是废话。。。又不是必须取到每个数字，一旦不合法不继续不就完了？
        # 本来先想到的是 sortedcontainer，后来想想堆就可以了。

        hp = list(zip([-a, -b, -c], ['a', 'b', 'c']))
        heapq.heapify(hp)
        res = ""
        while hp:
            tup = heapq.heappop(hp)
            if tup[0] == 0:
                return res
            if len(res) >= 2 and res[-1] == res[-2] == tup[1]:
                if not hp:
                    return res
                else:
                    tup2 = heapq.heappop(hp)
                    if tup2[0] == 0:
                        return res
                    else:
                        res += tup2[1]
                        # 本来当然是该减一，但是因为（Python的小根堆）这里都是负数，所以是加一。
                        if tup2[0] + 1 < 0:
                            heapq.heappush(hp, (tup2[0]+1, tup2[1]))
                heapq.heappush(hp, (tup[0], tup[1]))
            else:
                if tup[0] == 0:
                    return res
                else:
                    res += tup[1]
                if tup[0] + 1 < 0:
                    heapq.heappush(hp, (tup[0]+1, tup[1]))
        return res
        
"""
https://leetcode-cn.com/submissions/detail/265338105/

执行用时：28 ms, 在所有 Python3 提交中击败了89.66%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了53.10%的用户
通过测试用例：
34 / 34
"""
