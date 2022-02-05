class Solution(object):
    def minCostSetTime(self, startAt, moveCost, pushCost, targetSeconds):
        """
        :type startAt: int
        :type moveCost: int
        :type pushCost: int
        :type targetSeconds: int
        :rtype: int
        """
        
        mnt, sec = targetSeconds // 60, targetSeconds % 60
        
        l1 = list(map(int, list(str(mnt))))
        l2 = list(map(int, list(str(sec))))
        if len(l2) == 1:
            l2.insert(0, 0)
        
        res1 = 0
        pos1 = startAt
        ignoreZero = True
        if l1 != [0]:
            ignoreZero = False
            for num in l1:
                if pos1 == num:
                    res1 += pushCost
                else:
                    res1 += moveCost + pushCost
                    pos1 = num
        for num in l2:
            if ignoreZero and num == 0:
                continue
            else:
                ignoreZero = False
            if pos1 == num:
                res1 += pushCost
            else:
                res1 += moveCost + pushCost
                pos1 = num
        
        res2 = float('inf')
        # 此时还有第二种时间表示法
        if mnt >= 1 and sec < 40:
            mntNew = mnt - 1
            secNew = sec + 60
            l1New = list(map(int, list(str(mntNew))))
            l2New = list(map(int, list(str(secNew))))
            res2 = 0
            pos2 = startAt
            if l1New != [0]:
                for num in l1New:
                    if pos2 == num:
                        res2 += pushCost
                    else:
                        res2 += moveCost + pushCost
                        pos2 = num
            for num in l2New:
                if pos2 == num:
                    res2 += pushCost
                else:
                    res2 += moveCost + pushCost
                    pos2 = num
        
        return min(res1, res2)
    
"""
https://leetcode-cn.com/submissions/detail/265042286/

223 / 225 个通过测试用例
状态：解答错误

输入：
Hidden for this testcase during contest.
输出：
Hidden for this testcase during contest.
预期：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.

最后执行的输入：
1
9403
9402
6008
"""
