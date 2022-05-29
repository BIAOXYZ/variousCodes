from decimal import Decimal
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        def replace_price(price, discount):
            num1 = float(price[1:])
            num2 = num1 * (100 - discount) / 100
            res = Decimal(num2).quantize(Decimal("0.00"))
            res = '$' + str(res)
            return res
        ## print(replace_price('$23', 50))
        
        def is_price(word):
            return len(word) > 1 and word[0] == '$' and all(word[i].isdigit() for i in range(1, len(word)))
        
        lis = sentence.split()
        for i, word in enumerate(lis):
            if is_price(word):
                lis[i] = replace_price(word, discount)
        return ' '.join(lis)
    
"""
https://leetcode.cn/submissions/detail/319314714/

146 / 146 个通过测试用例
状态：通过
执行用时: 272 ms
内存消耗: 16.9 MB
"""
