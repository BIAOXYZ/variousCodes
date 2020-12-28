class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        def binarystrPlus1(s):
            """
            if s.count('0') = 0:
                pass
            
            # 如果写成上面那个就会报下述错误，应该是字符串不能用list的方法。。。
            SyntaxError: invalid syntax
                                ^
                if s.count('0') = 0:
            Line 10  (Solution.py)
            
            # 要换成类似下面的
            if '0' not in s:
            
            # 但是我试了试有的环境就可以啊。估计oj系统太腊鸡。
            num = ['0','0','0']
            str='0000'
            print num.count('0')  # 3
            print str.count('0')  # 4
            """
       
            # 该函数只在s为奇数时调用，所以上来flag就是1
            flag = 1
            n = length = len(s)
            
            # 字符串转成列表
            ls = list(s)
            
            while n - 1 >= 0:
                # 这个就是为处理还会增加新的位的情况，比如'111'，会返回'1000'
                if n - 1 == 0 and ls[n-1] is '1' and flag == 1: 
                    ls[n-1] = '0'
                    # 这句从 https://stackoverflow.com/questions/10631473/str-object-does-not-support-item-assignment-in-python 学的
                    s = ''.join(ls)
                    s = '1' + s
                    return s
                
                if ls[n-1] is '1' and flag == 1:
                    """ 
                    s[n-1] = '0'
                    
                    # 原来用上面那句会报：'str' object does not support item assignment
                    # str是immutable的，不能直接赋值。--> 了解这个，但是因为不熟，用的时候就踩坑，妈蛋。
                    """
                    ls[n-1] = '0'
                    n -= 1
                else:
                    ls[n-1] = '1'
                    break
            return ''.join(ls)
            
        step = 0
        while s is not '1':
            if s[-1] is '0':
                s = s[:-1]
                step += 1
            else:
                s = binarystrPlus1(s)
                step += 1
        return step

"""
提交结果：超出时间限制
0 / 73 个通过测试用例
最后执行的输入： "1101" 
"""
