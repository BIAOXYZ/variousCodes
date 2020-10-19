class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        length = len(s)
        if length < 4 or length > 12:
            return []
        segments = [0 for i in range(4)]
        res = []

        def dfs(segnum, pos):
            if segnum > 4:
                return
            elif segnum == 4:
                if pos == length:
                    ip = ".".join(str(seg) for seg in segments)
                    res.append(ip)
                    return
            elif segnum < 4:
                if pos == length:
                    return
                # 如果某段的开头是0，根据IP地址规则，只能立刻跳到下一段。
                elif s[pos] == '0':
                    segments[segnum] = 0
                    dfs(segnum+1, pos+1)
                else:
                    addr = 0
                    for end in range(pos, length):
                        addr = addr * 10 + (ord(s[end]) - ord("0"))
                        if 0 < addr <= 255:
                            segments[segnum] = addr
                            dfs(segnum + 1, end + 1)
                        else:
                            break
        dfs(0,0)
        return res
        
"""
https://leetcode-cn.com/submissions/detail/96355721/

147 / 147 个通过测试用例
状态：通过
执行用时：16 ms
内存消耗：12.8 MB
"""
"""
执行用时：16 ms, 在所有 Python 提交中击败了96.88%的用户
内存消耗：12.8 MB, 在所有 Python 提交中击败了36.36%的用户
"""
