class Solution:
    def grayCode(self, n: int) -> List[int]:

        """
        # 从[0,1]到[00,10,11,01]是怎么变的呢？先在0和1后面都贴上0，变为00和10。
        # 然后贴1的时候把顺序反转，变成从1和0的顺序贴，得到11和01。
        # 最终形成 [00,10,11,01]。
        # 这个的合理性不难想，假定 n-1 时已有 list 满足条件，那么当去构造 n 的 list 时：
        ## 先正向贴0，那么该差一个数字还是差一个数字，满足；
        ## 然后反过来，接头处一个贴0一个贴1，差一位不同，也满足；
        ## 最后贴1的那一半当然也满足。
        """

        if n == 1:
            return [0, 1]
        
        res = ['0', '1']
        m = 1
        while m < n:
            leftHalf = [res[i] + '0' for i in range(2**m)]
            rightHalf = [res[i] + '1' for i in range(2**m-1, -1, -1)]
            res = leftHalf + rightHalf
            m += 1
        return [int(elem, 2) for elem in res]
        
"""
https://leetcode-cn.com/submissions/detail/256146589/

执行用时：68 ms, 在所有 Python3 提交中击败了25.05%的用户
内存消耗：23.7 MB, 在所有 Python3 提交中击败了9.36%的用户
通过测试用例：
16 / 16
"""
