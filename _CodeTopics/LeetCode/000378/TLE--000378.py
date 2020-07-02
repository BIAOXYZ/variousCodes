class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        """
        [ 1,  5,  9]
        [10, 11, 13]
        [12, 13, 15]
        矩阵中所有元素去排序，其大小也有一定的规律，可以省时间。具体来说就是如果i'>i j'>j，
        那么必有 matrix[i'][j'] > matrix[i][j]。于是我们可以设定两个方向上的移动。比如最开始
        是1，然后水平方向上下一个元素是5，垂直方向上下一个元素是10。
        但是后来想想可能会面临某个新的水平方向的节点引入新的垂直方向节点的问题
        （其实还有到了边界拐弯的问题，但是这个还好）。
        总之太绕了，实在没时间。只能先用多路归并排序，最后有第k个元素就终止。
        """
        """
        n = len(matrix)
        mtr = [matrix[0][0]]
        vindex, hindex = [0,0], [0,0]
        while vindex <= [n-1, n-1] and hindex <= [n-1, n-1]:
            vertical = matrix[vindex[0]+1][vindex[1]]
            horizontal = matrix[hindex[0]][hindex[1]+1]
            if horizontal <= vertical:
                mtr.append(horizontal)
                hindex = [hindex[0],hindex[1]+1]
            else:
                mtr.append(vertical)
        """

        def twowaymerge(l1,l2):
            res = []
            while l1 and l2:
                if l1[0] <= l2[0]:
                    res.append(l1.pop(0))
                else:
                    res.append(l2.pop(0))
            if l1:
                res += l1
            if l2:
                res += l2
            return res

        length = len(matrix)
        res = []
        for i in range(length):
            res = twowaymerge(res, matrix[i])
        return res[k-1]
        
"""
https://leetcode-cn.com/submissions/detail/83964600/

83 / 85 个通过测试用例
状态：超出时间限制
"""
