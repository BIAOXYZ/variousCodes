
# -*- coding: utf-8 -*-
import sys
"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
总结：这道题开始没看清把输入当成个list去做了，走了些弯路。。。主体思想是逐个按位加，但是有些细节需要处理：
1.pre的引入，不然最后多出来的那个node没法删除，因为python所有对象都是引用，通过执行 cur = None 把cur设成空是不行的。
因为之前循环逐个节点加的时候最后还是给l多申请了一个ListNode(0)。只能通过倒回到前一个节点，然后把这个节点的next设为None才行。
2.代码写完后单步调没问题，但是运行就报错。提交到leetcode官方也accept了，所以一定是自己写的测试有啥问题。后来用pycharm调试，
发现并不是代码或者测试的问题，而是python版本的问题。同样的代码换python 2.7就没问题。于是立刻就明白了肯定是求除数那行代码的问题。

carryFlag = (l1.val + l2.val + carryFlag) / 10

用pycharm里的python 3.6.3跟了一下，题目自带的用例 342 + 465，第一次要计算 2 + 5。结果算出来的carryFlag就等于float型的0.77。。。
所以后面把这句换成能适应python3的写法吧。

carryFlag = (l1.val + l2.val + carryFlag) // 10

- python中的float除法和整除法 https://www.jianshu.com/p/9034aafb50aa
- 除法运算符/在Python2和Python3中的区别 https://www.pythontab.com/html/2017/pythonjichu_1227/1211.html
"""

# 为了本地调试需要把OJ系统里已定义好的ListNode类去掉注释添加进来。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carryFlag = 0
        l = ListNode(0)
        cur = l
        pre = l

        while l1 != None and l2 != None:
            cur.next = ListNode(0)
            cur.val = (l1.val + l2.val + carryFlag) % 10
            # carryFlag = (l1.val + l2.val + carryFlag) / 10  ## for python 2.x
            carryFlag = (l1.val + l2.val + carryFlag) // 10
            l1 = l1.next; l2 = l2.next; pre = cur; cur = cur.next

        if l1 == None and l2 == None:
            if carryFlag == 0:
                # pre是必须加的，不然到这一步没法倒退回去把最后一个node设成None。注意，这里用 cur = None 是不行的，因为python都是引用。
                # cur = None 只是把cur给变None了，但是l里最后这个node还是非None的。只能是用“把l的前一个node的next赋值为None的办法”，
                # 所以必须引入这个pre。
                pre.next = None
                return l
            else:
                cur.val = 1
                return l
        elif l1 == None and l2 != None:
            while l2 != None:
                cur.next = ListNode(0)
                cur.val = (l2.val + carryFlag) % 10
                carryFlag = (l2.val + carryFlag) // 10
                l2 = l2.next; pre = cur; cur = cur.next
            if carryFlag == 0:
                pre.next = None
                return l
            else:
                cur.val = 1
                return l       
        else:
            while l1 != None:
                cur.next = ListNode(0)
                cur.val = (l1.val + carryFlag) % 10
                carryFlag = (l1.val + carryFlag) // 10
                l1 = l1.next; pre = cur; cur = cur.next
            if carryFlag == 0:
                pre.next = None
                return l
            else:
                cur.val = 1
                return l

class Test(object):
    def run(self, l1, l2):
        sol = Solution()
        res = sol.addTwoNumbers(l1, l2)
        print("The input linked list are l1 = %s, l2 = %s and the result linked list is %s" % (l1, l2, res))
        print("The input num for linked list l1 is numl1 = %s, num for l2 is numl2 = %s and the result num for linked list is %s"
            % (Test().nodelistToNumber(l1), Test().nodelistToNumber(l2), Test().nodelistToNumber(res)))
    def numberToInputList(self, num = 0):
        pre = cur = testCase = ListNode(0)
        while num > 0:
            cur.val = num % 10
            num = num // 10
            cur.next = ListNode(0); pre = cur; cur = cur.next
        pre.next = None
        return testCase
    def nodelistToNumber(self, l):
        num = 0
        multiple = 1
        while l is not None:
            num += l.val * multiple
            l = l.next; multiple = multiple * 10
        return num
            
if __name__ == '__main__':
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")

    # 明天写个生成测试用力的函数，输入是整数或者list，生成ListNode组成的链表。
    # “测试用力”——可以的。。。窝这输入法- -
    l1 = ListNode(2); l1.next = ListNode(4); l1.next.next = ListNode(3)
    l2 = ListNode(5); l2.next = ListNode(6); l2.next.next = ListNode(4)
    test = Test()
    test.run(l1, l2)

    Test().run(Test().numberToInputList(12),Test().numberToInputList(345))
    Test().run(Test().numberToInputList(125),Test().numberToInputList(6789))
    Test().run(Test().numberToInputList(6789),Test().numberToInputList(98934))


    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")

