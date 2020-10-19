class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """

        """
        # 开始以为是dp，后来想想不对啊，dp虽说熟练后也挺套路的，但是简单题肯定用不到dp。
        所以更准确地说是肯定有不用dp的算法。

        # 然后分析了前面几个输入：
        1 - Alice先手负；2 - Alice先手胜；3 - Alice先手负；4 - Alice先手胜.....

        # 假设一直到2n-1, 2n时还符合这个规律，那么：
        - 对于2n+1，由于它是个奇数，不管Alice怎么选，第一次她选完会剩下一个偶数，Bob直接选个1，
          又剩了一个奇数给Alice，并且对这个奇数前面已经有结论了，因此Alice先手败。
        - 对于2n+2，Alice直接拿个1，给Bob留个2n+1，根据刚推出来的结论，Bob必败，因此Alice先手胜。
        因此对于2n+1和2n+2，也符合这个规律，所以整体就是这个规律。
        """

        if N % 2 == 0:
            return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/91159426/

40 / 40 个通过测试用例
状态：通过
执行用时：20 ms
内存消耗：12.9 MB
"""
"""
执行用时：20 ms, 在所有 Python 提交中击败了69.78%的用户
内存消耗：12.9 MB, 在所有 Python 提交中击败了100.00%的用户
"""
