class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        
        # 思路：其实就是分别找到水平方向和竖直方向上的最大差值，然后乘积即可。
        
        # 这个函数不能忘了处理收尾，其实也可以上了就把0和edgelen分别放到数组的收尾
        # 然后一个循环搞定。
        def maxDist(l,edgelen):
            maxdist = currdist = l[0] - 0
            for i in range(1,len(l)):
                ###print "currdist before is: ", currdist
                currdist = l[i] - l[i-1]
                ###print l[i],l[i-1]
                ###print "currdist after is: ", currdist
                maxdist = max(currdist, maxdist)
                ###print maxdist
            maxdist = max(edgelen-l[-1], maxdist)
            return maxdist
        
        horizontalCuts.sort()
        verticalCuts.sort()
        return (maxDist(horizontalCuts,h) * maxDist(verticalCuts,w)) % 1000000007
    
"""
# https://leetcode-cn.com/submissions/detail/75086391/

53 / 53 个通过测试用例
	状态：通过
执行用时：104 ms
内存消耗：22.9 MB
"""
"""
那个错的就不用看了，就是最后忘了去模一下 10^9+7，完全是低级失误。
但是没想到那个错误用例太长了，导致那个wrong answer的文件太大了。。。
"""
