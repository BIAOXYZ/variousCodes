class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        dic = {}
        luckylist = []
        for num in arr:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
            
            if dic[num] == num:
                luckylist.append(num)
            elif dic[num] != num and num in luckylist:
                luckylist.remove(num)
            else:
                continue
        
        """
        # ValueError: max() arg is an empty sequence
        if max(luckylist) > 0:
            return max(luckylist)
        else:
            return -1
        """
        
        """
        # ValueError: max() arg is an empty sequence
        if luckylist is []:
            return -1
        else:
            return max(luckylist
        """
        
        #return max(luckylist, -1)
        
        # if luckylist is []:  # 靠竟然是因为这个，is还不能完全替代==吗?
        if luckylist == []:
            return -1
        else:
            max = luckylist[0]
            for i in range(1, len(luckylist)):
                if luckylist[i] > max:
                    max = luckylist[i]
            return max
            
