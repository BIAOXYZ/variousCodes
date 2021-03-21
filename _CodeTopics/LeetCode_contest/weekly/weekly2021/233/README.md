
# 中国时间：2021-03-21 10:30

第 233 场周赛 https://leetcode-cn.com/contest/weekly-contest-233
- 5709. 最大升序子数组和 https://leetcode-cn.com/contest/weekly-contest-233/problems/maximum-ascending-subarray-sum/
- 5710. 积压订单中的订单总数 https://leetcode-cn.com/contest/weekly-contest-233/problems/number-of-orders-in-the-backlog/
- 5711. 有界数组中指定下标处的最大值 https://leetcode-cn.com/contest/weekly-contest-233/problems/maximum-value-at-a-given-index-in-a-bounded-array/
- 5696. 统计异或值在范围内的数对有多少 https://leetcode-cn.com/contest/weekly-contest-233/problems/count-pairs-with-xor-in-a-range/

# 笔记

## (2)

第二题开始想着字典或者双端队列，但是感觉都会超时。于是换成用堆，等堆的实现写完了发现应该一个用大根堆一个用小根堆，真是艹了。。。于是开始怀疑是不是自己想复杂了，又重新用字典写，结果就是超时了。。。淦！

这个是没提交的heapq的实现，其实当时也可以选择坚持这条路线，对于两个堆里的价格一个用正数一个用负数（从而相当于一个大根堆一个小根堆）。但是这他么就是路线选择问题了啊。。。

**TODO**：
```py
from heapq import *
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        
        buyheap = []
        sellheap = []
        heapify(buyheap)
        heapify(sellheap)
        if orders[0][2] == 0:
            heappush(buyheap, [orders[0][0], orders[0][1]])
        else:
            #selldic[orders[0][0]] = orders[0][1]
            heappush(sellheap, [orders[0][0], orders[0][1]])
        
        for i in range(1, len(orders)):
            od = orders[i]
            if od[2] == 0:
                while od[1] > 0 and sellheap:
                    tmpod = heappop(sellheap)
                    if od[0] >= tmpod[0]:
                        if od[1] >= tmpod[1]:
                            od[1] -= tmpod[1]
                        else:
                            heappush(sellheap, [tmpod[0], tmpod[1]-od[1]])
                            break
                    else:
                        heappush(sellheap, tmpod)
                        heappush(buyheap, [od[0], od[1]])
                        break
            elif od[2] == 1:
                while od[1] > 0 and buyheap:
                    tmpod = heappop(buyheap)
                    if od[0] >= tmpod[0]:
                        if od[1] >= tmpod[1]:
                            od[1] -= tmpod[1]
                        else:
                            heappush(buyheap, [tmpod[0], tmpod[1]-od[1]])
                            break
                    else:
                        heappush(buyheap, tmpod)
                        heappush(sellheap, [od[0], od[1]])
                        break                    
        res = 0
        while buyheap:
            tmpod = heappop(buyheap)
            res += tmpod[1]
        while sellheap:
            tmpod = heappop(sellheap)
            res += tmpod[1]
        return res % (10**9+7)
```
