class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        
        # 这里最好先处理旋转。
        def stone_fall(lis, n):
            stk = []
            for i in range(n-1, -1, -1):
                if lis[i] == ".":
                    stk.append(i)
                elif lis[i] == "*":
                    stk = []
                elif lis[i] == "#":
                    if stk:
                        j = stk.pop(0)
                        lis[i], lis[j] = lis[j], lis[i]
                        stk.append(i)
                        # 草，被这deque给坑了，就为了提升那一点速度，结果deque没有sort方法，害我最后没提交上。
                        stk.sort(reverse=True)
        
        rownum, colnum = len(box), len(box[0])
        for row in box:
            stone_fall(row, colnum)
        
        res = [[0 for _ in range(rownum)] for _ in range(colnum)]
        for i in range(colnum):
            for j in range(rownum):
                # 注意是90旋转，不是转置！
                res[i][j] = box[rownum-1-j][i]
        return res
    
"""
https://leetcode-cn.com/submissions/detail/177825978/

87 / 87 个通过测试用例
状态：通过
执行用时: 784 ms
内存消耗: 56.7 MB
"""
