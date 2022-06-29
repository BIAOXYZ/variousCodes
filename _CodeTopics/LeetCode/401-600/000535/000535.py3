class Codec:
    
    def __init__(self) -> None:
        self.ctr = 0
        self.prefix = "http://tinyurl.com/"
        self.dic1 = {}
        self.dic2 = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.dic1:
            return self.dic1[longUrl]
        self.ctr += 1
        self.dic1[longUrl] = self.prefix + str(self.ctr)
        self.dic2[self.dic1[longUrl]] = longUrl
        return self.dic1[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic2[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

"""
https://leetcode.cn/submissions/detail/330595429/

执行用时：
32 ms
, 在所有 Python3 提交中击败了
96.89%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
68.00%
的用户
通过测试用例：
739 / 739
"""
