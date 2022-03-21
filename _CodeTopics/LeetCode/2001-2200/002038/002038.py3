class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # 只要还有连续三个相同字母，就能操作一次；连续四个相同字母，操作两次。
        # 所以就是看谁的三连多了。一样多的话 Alice 吃亏。。。
        
        def get_start_pos_and_len(s, ch):
            dic = {}
            state = [False, -1, -1]
            for i in range(len(s)):
                if s[i] == ch:
                    if not state[0]:
                        state = [True, i, 1]
                    else:
                        state[2] += 1
                else:
                    if not state[0]:
                        continue
                    else:
                        dic[state[1]] = state[2]
                        state = [False, -1, -1]
            if state[0]:
                dic[state[1]] = state[2]
            return dic
        
        dicA = get_start_pos_and_len(colors, 'A')
        dicB = get_start_pos_and_len(colors, 'B')
        totalA = sum(0 if num < 3 else num - 2 for num in dicA.values())
        totalB = sum(0 if num < 3 else num - 2 for num in dicB.values())
        return totalA > totalB
        
"""
https://leetcode-cn.com/submissions/detail/287268429/

执行用时：336 ms, 在所有 Python3 提交中击败了23.47%的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了5.10%的用户
通过测试用例：
83 / 83
"""
"""
注：这个统计字符串中某个字符的起始位置和长度的函数感觉写得还可以，比之前另一场
比赛里匆忙写出来的要好多了（随便找了找，已经找不到那个版本了，就只记得这个版本吧）。
"""
