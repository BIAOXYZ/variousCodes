class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        length = len(price)

        usefulGiftPackage = []
        for sp in special:
            if sum(sp[i] * price[i] for i in range(length)) > sp[-1] and sum(sp[i] for i in range(length)) > 0:
                usefulGiftPackage.append(sp)
        
        dic = {}
        def memorize_search(curr_needs):
            curr_needs_tuple = tuple(curr_needs)
            if dic.has_key(curr_needs_tuple):
                return dic[curr_needs_tuple]
            min_price = sum(price[i] * need for i, need in enumerate(curr_needs))
            for curr_sp in usefulGiftPackage:
                next_needs = []
                for i in range(length):
                    if curr_sp[i] > curr_needs[i]:
                        break
                    next_needs.append(curr_needs[i] - curr_sp[i])
                if len(next_needs) == length:
                    min_price = min(min_price, memorize_search(next_needs) + curr_sp[-1])
            dic[curr_needs_tuple] = min_price
            return min_price
        
        return memorize_search(needs)
        
"""
https://leetcode-cn.com/submissions/detail/231857871/

执行用时：32 ms, 在所有 Python 提交中击败了100.00%的用户
内存消耗：13.3 MB, 在所有 Python 提交中击败了15.79%的用户
通过测试用例：64 / 64
"""
