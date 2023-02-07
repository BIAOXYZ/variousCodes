class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        ddic = defaultdict(list)
        n = len(keyName)
        for i in range(n):
            name, time = keyName[i], keyTime[i]
            ddic[name].append(time)
        
        def within_one_hour(t1, t2):
            hourDiff = int(t2[:2]) - int(t1[:2])
            minuteDiff = int(t2[3:]) >= int(t1[3:])
            if hourDiff >= 2:
                return False
            elif hourDiff == 1:
                if minuteDiff > 0:
                    return False
            return True

        res = []
        for name, times in ddic.items():
            if len(times) < 3:
                continue
            times.sort()
            for i in range(2, len(times)):
                if within_one_hour(times[i-1], times[i]) and within_one_hour(times[i-2], times[i-1]):
                    res.append(name)
                    break
        return sorted(res)
        
"""
https://leetcode.cn/submissions/detail/400119152/

28 / 77 个通过测试用例
状态：解答错误

输入：
["a","a","a","a","b","b","b","b","b","b","c","c","c","c"]
["01:35","08:43","20:49","00:01","17:44","02:50","18:48","22:27","14:12","18:00","12:38","20:40","03:59","22:24"]
输出：
["b"]
预期结果：
[]
"""
