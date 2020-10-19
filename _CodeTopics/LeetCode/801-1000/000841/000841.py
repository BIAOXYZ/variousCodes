class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        visited = []

        def dfs_for_room_i(i):
            if i in visited:
                return
            visited.append(i)
            for roomNum in rooms[i]:
                dfs_for_room_i(roomNum)
            return
        
        dfs_for_room_i(0)
        return len(visited) == len(rooms)
        
"""
https://leetcode-cn.com/submissions/detail/103207682/

67 / 67 个通过测试用例
状态：通过
执行用时: 76 ms
内存消耗: 13.8 MB
"""
"""
执行用时：76 ms, 在所有 Python 提交中击败了14.75%的用户
内存消耗：13.8 MB, 在所有 Python 提交中击败了6.06%的用户
"""
