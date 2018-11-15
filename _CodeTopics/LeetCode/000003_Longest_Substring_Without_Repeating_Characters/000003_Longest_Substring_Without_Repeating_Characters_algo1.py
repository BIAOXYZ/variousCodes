
# -*- coding: utf-8 -*-
import sys
"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
总体思路是把s里所有的子串s[i:j]一一列举出来，然后对子串中的每一个元素s[i:j][k]调用字符串的count方法，
看当前字符s[i:j][k]有没有在s[i:j]中出现两次或两次以上。如果有这个字符串就不能算数，如果没有就比较当前
的s[i:j]的长度和maxSubstrLen哪个更大，作为新的maxSubstrLen的值。最后所有循环结束，返回maxSubstrLen。
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """ 一个用例'dvdf'让我发现我之前题意理解有问题，以为出现重复字符后新的子串一定是从重复字母开始。所以干脆重写了。先用蛮力搜索搞定再说吧。

        maxSubstrLen = 0
        curSubstr = ""
        # -- 最开始没有考虑这个变量，发现程序是不对的，对于没有重复字母的字符串比如"abc"，最后的返回值会是0。
        #    因为第一个分支压根就不进去！结果最后返回值maxSubstrLen还是初始值0。所以增加这个变量，如果最后一直
        #    是True，说明整个字符串没有重复字符，所以此时返回值应该是这个字符串的长度。
        noRepeatCharacter = True
        for i in range(len(s)):
            if s[i] in curSubstr:
                 # -- Python里没有类似C语言问号一样的三目操作符 expression1 ? expression2 : expression3
                 #    所以这里用 true_part if condition else false_part 代替
                 maxSubstrLen = maxSubstrLen if len(curSubstr) <= maxSubstrLen else len(curSubstr)
                 curSubstr = s[i]
                 noRepeatCharacter = False
            else:
                curSubstr = curSubstr + s[i]
        if noRepeatCharacter:
            return len(s)
        else:
            # -- return maxSubstrLen
            #    最开始就是上面这句，对于输入"aab"返回值是1而不是2。原因是想想就明白了：第二个a进if分支，然后maxSubstrLen为1。接着
            #    b进入else分支，curSubstr为"ab"，程序跳出for循环。但是maxSubstrLen不会再加一了，此时curSubstr的长度比maxSubstrLen
            #    更大。所以把最后return这里改一下，防止这种情况。
            return maxSubstrLen if len(curSubstr) <= maxSubstrLen else len(curSubstr)
        """

        # 打算先用brute force搞定再说。
        maxSubstrLen = 0

        # 这里range到len(s)-1就行了，没必要到len(s)
        # 麻蛋。。。用len(s)-1还不行，单字符过不去。。。本来长度为1，结果输出0。应该是range(0)的话i没法取值，直接跳到最后return那步了。
        for i in range(len(s)):
            # -- 这里开始错了一下，最开始写的是 for j in range(i+1, len(s)):
            #    这种写法这所以不对是因为会导致最后一个字符取不着，比如s="come"的话会导致最外层for循环的第一轮到"com"就循环完了。
            #    其实就是python的range()和string[]容易搞混。再加上计算机下标从0开始，人比较习惯从1开始。这里还是小总结一下：
            #    不管range(start, end), range(end), string[start:end]等，总之end的值都取不到。所以尽量按机器的方式去“定位”下标：
            #    str="abcdef"
            #         |||||| 
            #    pos="012345"
            #    所以取str[2:4]的时候就是取str的index从2到4的，但是4不取，所以是"cd"
            for j in range(i+1, len(s)+1):
                noRepeatCharacter = True
                for k in range(j-i):
                    # 这里也可以用 in 的办法： 
                    if s[i:j].count(s[i:j][k]) >= 2:
                        noRepeatCharacter = False
                        break
                if noRepeatCharacter:
                    maxSubstrLen = max(maxSubstrLen, len(s[i:j]))
        return maxSubstrLen


class Test():
    def run(self, s):
        sol = Solution()
        res = sol.lengthOfLongestSubstring(s)
        print ("The max length of input string %s is %d." % (s, res))

if __name__=="__main__":
    print("------------------------------\nThe main program will start!\n------------------------------\n")
    print("The default coding is:", sys.getdefaultencoding())
    print("\n")

    test = Test()

    # examples/test cases from the problem
    test.run("abcabcbb")
    test.run("bbbbb")
    test.run("pwwkew")

    # self-designed test cases
    test.run('come')
    test.run("a1b")
    test.run("xyz#!")
    test.run('t')
    test.run(" ")
    test.run(" a ")

    # not passed test cases
    test.run('aab')
    test.run('dvdf')

    # 麻丹，用brute force的话这个用例超时了。。。劳资本地运行好着呢，结果是11美滋滋。
    test.run("gjbbcubrxapxmkveaiombckftocwaifitgjwdnpapezbqwhqhvdizpotdspfcwpxfbtiqikfolieipxpmazmrphxj")

    # 919 / 987 test cases passed.
    # 提了一次还是超时。。。本地跑结果是13
    test.run("otpubyjbulayglneiafxcvsqepewrnpgggcjelmbypbeaqliqqhvlzlsqpqiefqnlsysfntdcwhenuodkvyywlsociwjno")

    # 973 / 987 test cases passed.
    # 期望输出1，开始错误输出0 --> nnd，空格本就应该不算啊~
    test.run(" ")

    # 气死了，明明solution里有用brute force的，结果来了个用例我感觉得有几万个字符，都不敢复制。。。算了，换一种brute force的办法吧。
    # 这个程序正确性上应该没问题，就是他么被坑。。。
    test.run("")

    print("\n")
    print("------------------------------\nThe main program has ended!\n------------------------------\n")
