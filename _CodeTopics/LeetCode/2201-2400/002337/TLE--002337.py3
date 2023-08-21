class Solution:
    def canChange(self, start: str, target: str) -> bool:

        def can_right_move(s1, s2):
            # 只有这几类情况下，当前字符能和紧邻着的右边的字符交换
            if (s1 == '_' and s2 in ['_', 'L']) or \
                (s1 == 'R' and s2 in ['_', 'R']) or \
                (s1 == 'L' and s2 == 'L'):
                return True
            return False

        n = len(start)
        start, target = list(start), list(target)
        pos1 = pos2 = 0
        while pos2 < n:
            while pos1 < n and start[pos1] != target[pos2]:
                # 只有能和右边紧邻着的字符交换，才能继续加1
                if pos1 < n-1 and can_right_move(start[pos1], start[pos1 + 1]):
                    pos1 += 1
                else:
                    return False
            if pos1 == n:
                return False
            start[pos1], start[pos2] = start[pos2], start[pos1]
            pos2 += 1
            pos1 = pos2
        return True
        
"""
https://leetcode.cn/problems/move-pieces-to-obtain-a-string/submissions/458580328/

超出时间限制
8 / 131 个通过的测试用例
"""
