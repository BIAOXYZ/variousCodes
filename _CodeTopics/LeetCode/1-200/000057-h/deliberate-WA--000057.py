class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        """
        # 这个会错的原因应该是假定了intervals里的每个区间的右端点也有序？
        # 比如目前看下面这个官方用例可以跑过：
        [[1,2],[3,5],[6,7],[8,10],[12,16]]
        [4,8]

        # 但是我稍微改一下，改成每个右区间端点没有严格顺序就跑不过了
        [[1,2],[3,11],[6,7],[8,10],[12,16]]
        [4,8]

        # 不过先不管了，先提了准备睡觉了。
        """

        length = len(intervals)
        res = []
        left, right = newInterval[0], newInterval[1]
        flag = 'left'

        for i in range(length):
            currSmall, currBig = intervals[i][0], intervals[i][1]
            if flag == 'left':
                if left > currBig:
                    res.append(intervals[i])
                elif currSmall <= left <= currBig:
                    newleft = currSmall
                    flag = 'right'
                elif left < currSmall:
                    newleft = left
                    flag = 'right'
            if flag == 'right':
                if right < currSmall:
                    newright = right
                    res.append([newleft, newright])
                    flag = 'end'
                elif currSmall <= right <= currBig:
                    newright = currBig
                    res.append([newleft, newright])
                    flag = 'end'
                    continue
                elif right > currBig:
                    continue
            if flag == 'end':
                res.append(intervals[i])
        return res
        
"""
https://leetcode-cn.com/submissions/detail/120858603/

83 / 156 个通过测试用例
状态：解答错误

输入：
[]
[5,7]
输出：
[]
预期：
[[5,7]]
"""
