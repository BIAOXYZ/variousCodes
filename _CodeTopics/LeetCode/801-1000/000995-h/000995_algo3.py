class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        length = len(A)
        total = 0
        currReverseNum = 0
        """
        # diffArr = [0 for _ in range(length+1)]
        # 上面这句就是差分数组申请的语句，但是实际上差分数组也可以不用：对于位置i来说，如果i在 [0,K) 之内，它之前累积的翻转
        # 情况完全可以通过 currReverseNum 传递过去。但是假如位置i处于大于等于K的位置，除了考虑 currReverseNum 传导过去的影响，
        # 还得额外考虑下第 i-K 个位置的影响（但是介于 i-K 和 i 之间的就不用考虑了，因为会通过 currReverseNum 传导过来）。

        # 我们举例如下： [0,0,0,1,x,y,z]，K = 3。后面的x、y、z随便啥值都行。
        ## 位置0对应的currReverseNum应为1，然后经过位置1和位置2都保持不变，还是1。来到位置3时，如果currReverseNum还是1，那就
        ## 意味着需要对位置3进行翻转（因为此时 A[3] ^ currReverseNum 为0），但是位置3上是1，明显不应该翻转的。造成这种情况的原因是：
        ## 位置0的翻转，按照之前差分数组的思路，会让位置3上的1受影响（也就是在传导过来的currReverseNum基础上再异或1）。

        ## 现在，我们考虑前面提到的位置 i-K 型（3-3=0）的影响：对于位置3来说，因为位置0翻转了，
        ## 所以除了传过来的 currReverseNum，这个的翻转也必须考虑进去。
        ## 那么就是两个1，也就是不翻转了，这时就对了。
        """

        for i in range(length):
            if i >= K and A[i-K] >= 2:
                currReverseNum ^= 1
                A[i-K] -= 2
            if A[i] ^ currReverseNum == 0:
                if i + K > length:
                    return -1
                total += 1
                A[i] += 2
                currReverseNum ^= 1
        return total
        
"""
https://leetcode-cn.com/submissions/detail/147429023/

110 / 110 个通过测试用例
状态：通过
执行用时: 724 ms
内存消耗: 14.4 MB

执行用时：724 ms, 在所有 Python 提交中击败了72.76%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了61.86%的用户
"""
