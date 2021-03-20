class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.mp = {}
        self.live = timeToLive

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.mp[tokenId] = currentTime + self.live

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.mp and currentTime < self.mp[tokenId]:
            self.mp[tokenId] = currentTime + self.live

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        res = 0
        for v in self.mp.values():
            if currentTime < v:
                res += 1
        return res


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

"""
https://leetcode-cn.com/submissions/detail/157686015/

90 / 90 个通过测试用例
状态：通过
执行用时: 544 ms
内存消耗: 14.3 MB
"""
