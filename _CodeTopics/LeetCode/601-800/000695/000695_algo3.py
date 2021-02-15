class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # DFS + 栈
        # 注意这个和BFS非常像，但是就是因为往外pop()的顺序不同，结果造成了本质是不一样的：
        # BFS用的存储对象本质上是个（先进先出的）队列；而 DFS+栈 从名字就看出来了，存储用的是（后进先出的）栈。
        # 用队列一定是离最开始那个点层数上越近的越先pop()出来，从而达到BFS的效果。
        # 而用栈稍微有那么一点点难理解为什么就能达到DFS的效果，但是想想就知道了：每次pop的是最后加入的，
        # 那么现在假设初始点是0层的0，并假设此时栈里是[01,02]，然后02出栈，
        # 02连着的（会有下一层，当然也可能会有01，但是不管这些）会进栈，不妨假定变成了[01,001,002,003]。
        # 如此往复，01虽然也是第一层的，但是要到02连着的全遍历完了才能到它，这不就是DFS么。

        def is_legal_coordinate_v2(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs_with_stack_and_count_one(coor):
            numOfOne = 0
            stk = [coor]
            while stk:
                currCoor = stk.pop()
                x, y = currCoor[0], currCoor[1]
                neighbors = [[x-1,y], [x+1,y], [x,y-1], [x,y+1]]
                for neighbor in neighbors:
                    newx, newy = neighbor[0], neighbor[1]
                    if is_legal_coordinate_v2(newx, newy) and grid[newx][newy] == 1 and [newx,newy] not in visited:
                        visited.append([newx,newy])
                        numOfOne += 1
                        stk.append([newx,newy])
            return numOfOne

        rows, cols = len(grid), len(grid[0])
        visited = []
        maxArea = currArea = 0

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1 and [x,y] not in visited:
                    visited.append([x,y])
                    currArea += 1
                    currArea += dfs_with_stack_and_count_one([x,y])
                    maxArea = max(maxArea, currArea)
                    currArea = 0
        return maxArea
        
"""
https://leetcode-cn.com/submissions/detail/145947640/

726 / 726 个通过测试用例
状态：通过
执行用时: 1012 ms
内存消耗: 13.4 MB

执行用时：1012 ms, 在所有 Python 提交中击败了5.22%的用户
内存消耗：13.4 MB, 在所有 Python 提交中击败了84.74%的用户
"""
