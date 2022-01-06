class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        MOUSE_WIN, CAT_WIN, DRAWN = 1, 2, 0

        n = len(graph)
        # 三维dp数组的意义分别是： dp[mouse][cat][round]
        # 其中round达到 2n 时，说明双方都已经没有什么更好的策略了，
        # 因此最佳就是平局，详情可参见官方答案。
        dp = [[[-1 for _ in range(2*n)] for _ in range(n)] for _ in range(n)]

        def get_result(mousePos:int, catPos:int, round:int) -> int:
            if round == 2*n:
                return DRAWN
            if dp[mousePos][catPos][round] != -1:
                return dp[mousePos][catPos][round]
            tmpRes = -1
            if mousePos == catPos and catPos != 0:
                tmpRes = CAT_WIN
            elif mousePos == 0:
                tmpRes = MOUSE_WIN
            else:
                tmpRes = get_next_result(mousePos, catPos, round)
            dp[mousePos][catPos][round] = tmpRes
            return tmpRes

        def get_next_result(mousePos:int, catPos:int, round:int) -> int:
            currPos = mousePos if round % 2 == 0 else catPos
            # 当前是谁移动，先假定默认结果是谁输（因为移动过程中只要有一个更好的结果，就会更正过来）
            defaultBadRes = CAT_WIN if currPos == mousePos else MOUSE_WIN
            res = defaultBadRes
            for nextPos in graph[currPos]:
                if currPos == catPos and nextPos == 0:
                    continue
                nextMousePos = nextPos if round % 2 == 0 else mousePos
                nextCatPos = nextPos if round % 2 == 1 else catPos
                nextRes = get_result(nextMousePos, nextCatPos, round + 1)
                # 这下面几行代码还是挺不错的，兼顾了老鼠和猫的情况。自己想改一个，感觉暂时也没有更清晰的改法了。
                if nextRes != defaultBadRes:
                    res = nextRes
                    if res != DRAWN:
                        break
            return res

        return get_result(1, 2, 0)
        
"""
https://leetcode-cn.com/submissions/detail/255795496/

执行用时：576 ms, 在所有 Python3 提交中击败了17.45%的用户
内存消耗：26.8 MB, 在所有 Python3 提交中击败了31.70%的用户
通过测试用例：
52 / 52
"""
