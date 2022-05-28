class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        sub_alphabeta = [chr(i) for i in range(ord('a'), ord('f')+1)]
        sub_Alphabeta = [chr(i) for i in range(ord('A'), ord('F')+1)]
        number = [chr(i) for i in range(ord('0'), ord('9')+1)]
        legal = sub_alphabeta + sub_Alphabeta + number

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
https://leetcode.cn/submissions/detail/319249832/

执行用时：
36 ms
, 在所有 Python3 提交中击败了
70.15%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
20.91%
的用户
通过测试用例：
73 / 73
"""
