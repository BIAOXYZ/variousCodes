class Solution:
    def validUtf8(self, data: List[int]) -> bool:

        def utf8_type(num : int) -> int:
            if 0 <= num <= 127: return 0
            elif 192 <= num <= 223: return 1
            elif 224 <= num <= 239: return 2
            elif 240 <= num <= 247: return 3
            elif 128 <= num <= 191: return -1
            else: return -2
        
        n = len(data)
        ind = 0
        flag = 0
        while ind < n:
            ch, chType = data[ind], utf8_type(data[ind])
            if flag == 0:
                if chType not in [0,1,2,3]:
                    return False
                flag = chType
                ind += 1
            elif flag > 0:
                while ind < n and flag > 0:
                    if chType != -1:
                        return False
                    flag += chType
                    ind += 1
                    ch, chType = data[ind], utf8_type(data[ind])
        if flag != 0:
            return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/282073090/

5 / 49 个通过测试用例
状态：执行出错

执行出错信息：
IndexError: list index out of range
    ch, chType = data[ind], utf8_type(data[ind])
Line 28 in validUtf8 (Solution.py)
    ret = Solution().validUtf8(param_1)
Line 53 in _driver (Solution.py)
    _driver()
Line 64 in <module> (Solution.py)
最后执行的输入：
[230,136,145]
"""
