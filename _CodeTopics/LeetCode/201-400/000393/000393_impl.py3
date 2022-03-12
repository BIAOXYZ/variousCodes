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
            elif flag > 0:
                if chType != -1:
                    return False
                flag += chType
            ind += 1
        return False if flag != 0 else True
        
"""
https://leetcode-cn.com/submissions/detail/282073846/

执行用时：44 ms, 在所有 Python3 提交中击败了71.43%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了70.07%的用户
通过测试用例：
49 / 49
"""
