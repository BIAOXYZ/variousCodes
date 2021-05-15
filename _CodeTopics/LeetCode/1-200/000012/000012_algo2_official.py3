class Solution:
    VALUE_SYMBOLS = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]
    def intToRoman(self, num: int) -> str:
        res = []
        # 一是为了这个直接 `Solution.变量` 的用法；二是答案的模拟太牛氓了。。。其实我的那个实现才更算“模拟”。。。
        for val, symbol in Solution.VALUE_SYMBOLS:
            while num >= val:
                res.append(symbol)
                num -= val
            if num == 0:
                break
        return "".join(res)
        
"""
https://leetcode-cn.com/submissions/detail/177682113/

3999 / 3999 个通过测试用例
状态：通过
执行用时: 64 ms
内存消耗: 14.9 MB
"""
