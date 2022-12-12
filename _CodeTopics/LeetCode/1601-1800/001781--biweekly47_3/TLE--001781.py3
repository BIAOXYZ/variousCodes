class Solution:
    def beautySum(self, s: str) -> int:

        # 第 47 场双周赛第三题

        # 就为了上个前缀和（从而和比赛时的算法不一样），麻烦死了。。。还不如暴力呢——关键和暴力复杂度也一样- -

        n = len(s)
        tmpLis = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            ch = s[i]
            for j in range(i, n):
                tmpLis[j][ord(ch)-ord('a')] += 1
        ## print(tmpLis)
        
        res = 0
        for left in range(n-2):
            for right in range(left+2, n):
                l1 = tmpLis[left]
                l2 = tmpLis[right]
                tmp = [l2[i] - l1[i] + int(ord(s[left]) - ord('a') == i) for i in range(26)]
                maxElem = max(tmp)
                for i in range(26):
                    if tmp[i] == 0:
                        tmp[i] = float('inf')
                res += maxElem - min(tmp)
        return res
        
"""
https://leetcode.cn/submissions/detail/388755154/

51 / 57 个通过测试用例
状态：超出时间限制

最后执行的输入：
"knlzzhnfltqakxnlixytpvaqlqevyrprgxiorsvkapjmlcrwcekputnzaxxffeqqqzvtdcldoeyqbehsfztsopjqzujzekbinwfkoeajszactvxutjqeldcccmxlgdunkimvlxiykgsxtchhtshrmacrpiqiqfftchsznupfxzcaedpcxnbysyacwzlumpbvzptqtrzojiqscjfggylwoxchjxjcylukbjikyidfiqxqtsaqpfabuenbmdmrcirfmzcnhjpfetjitpomjwixgcqcjjquqfpkhmggpsnlacnubytpytjvjovurlciewbumgnjaemivtehdmoshrhjeeogowcuetxhkivtawhlttajodbwdvhcctbeikcokxouvvgtiayzitevaazkovujcssbesgyihbitzxsauuyssaduengrkhdhwoshdcdvxdrkewnyismpvrxqfo"
"""
