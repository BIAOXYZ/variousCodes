class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        alphabeta = [chr(i) for i in range(ord('a'), ord('z')+1)]
        Alphabeta = [chr(i) for i in range(ord('A'), ord('Z')+1)]
        number = [chr(i) for i in range(ord('0'), ord('9')+1)]
        legal = alphabeta + Alphabeta + number

        def is_ipv4(queryIP):
            lis = queryIP.split('.')
            if len(lis) != 4:
                return False
            for seg in lis:
                if seg[0] == '0' and len(seg) > 1:
                    return False
                for ch in seg:
                    if ch not in number:
                        return False
                if int(seg) > 255:
                    return False
            return True

        def is_ipv6(queryIP):
            lis = queryIP.split(':')
            if len(lis) != 8:
                return False
            for seg in lis:
                if len(seg) > 4 or len(seg) < 1:
                    return False
                for ch in seg:
                    if ch not in legal:
                        return False
            return True

        # 单行的三重（甚至是多重）if表达式
        return "IPv4" if is_ipv4(queryIP) else "IPv6" if is_ipv6(queryIP) else "Neither"
        
"""
https://leetcode.cn/submissions/detail/319249227/

8 / 73 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: string index out of range
    if seg[0] == '0' and len(seg) > 1:
Line 14 in is_ipv4 (Solution.py)
    return "IPv4" if is_ipv4(queryIP) else "IPv6" if is_ipv6(queryIP) else "Neither"
Line 36 in validIPAddress (Solution.py)
    ret = Solution().validIPAddress(param_1)
Line 58 in _driver (Solution.py)
    _driver()
Line 69 in <module> (Solution.py)
最后执行的输入：
"1.0.1."
"""
