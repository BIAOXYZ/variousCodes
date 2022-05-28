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
                if not seg or (seg[0] == '0' and len(seg) > 1):
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
https://leetcode.cn/submissions/detail/319249661/

69 / 73 个通过测试用例
状态：解答错误

输入：
"20EE:FGb8:85a3:0:0:8A2E:0370:7334"
输出：
"IPv6"
预期结果：
"Neither"
"""
