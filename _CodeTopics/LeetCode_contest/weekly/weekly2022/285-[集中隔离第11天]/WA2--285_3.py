class Solution(object):
    def maximumBobPoints(self, numArrows, aliceArrows):
        """
        :type numArrows: int
        :type aliceArrows: List[int]
        :rtype: List[int]
        """
        
        # 位运算列举，当前位是1，表示 bob 赢下这个位置（当然要用最小代价）
        # 所以可能出出现有些情况是赢不下来的。
        
        n = 12
        maxscore = 0
        res = []
        for bitmap in range(1 << n):
            curr = numArrows
            subset = []
            flag = 1
            for i in range(n):
                if (bitmap >> i) & 1 == 1:
                    if curr > aliceArrows[i]:
                        curr -= aliceArrows[i]+1
                        subset.append(aliceArrows[i]+1)
                    else:
                        flag = 0
                        break
                else:
                    subset.append(0)
            if flag:
                score = 0
                for i in range(n):
                    if (bitmap >> i) & 1 == 1:
                        score += i
                if score > maxscore:
                    maxscore = score
                    res = subset
        return res
    
"""
https://leetcode-cn.com/submissions/detail/286244158/

41 / 173 个通过测试用例
状态：解答错误

输入：
89
[3,2,28,1,7,1,16,7,3,13,3,5]
输出：
[0,3,0,2,8,2,17,8,4,14,4,6]
预期：
[21,3,0,2,8,2,17,8,4,14,4,6]
"""
