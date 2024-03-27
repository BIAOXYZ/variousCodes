class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:

        MOD = 10**9 + 7
        n = len(nextVisit)

        # 房间号 : 访问次数(奇数or偶数) 
        visited = {}
        room_no = 0
        day = 0

        # python 模拟 do-while 的常用方式
        while True:
            if room_no not in visited:
                visited[room_no] = 1
                room_no = nextVisit[room_no]
            else:
                visited[room_no] = (visited[room_no] + 1) % 2
                if visited[room_no] % 2 == 0:
                    room_no = (room_no + 1) % n
                else:
                    room_no = nextVisit[room_no]
            if len(visited) == n:
                break
            day += 1
        return day
        
"""
https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/submissions/517473981?envType=daily-question&envId=2024-03-28

超出时间限制
30 / 239 个通过的测试用例

超出时间限制
30 / 239 个通过的测试用例
最后执行的输入
添加到测试用例
nextVisit =
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
"""
