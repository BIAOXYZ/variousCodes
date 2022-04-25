class TreeNode(object):
    def __init__(self, s):
        self.val = s
        self.children = [] 

class Solution:
    def lengthLongestPath(self, input: str) -> int:

        if '.' not in input:
            return 0

        def get_level(s):
            level = 0
            for i in range(len(s)):
                # 开始还按两个字符去处理了，实际上是转义字符和字母，
                # 也就是 '\t' 一起算一个字符。
                if s[i] == '\t':
                    level += 1
                else:
                    break
            return level
        
        lis = input.split('\n')
        dummyRoot = TreeNode('')
        # 表示当前最邻近的第 0, 1, 2, 3, ... 层节点。那么新的节点去找父亲的时候，肯定是这里面的某一个。
        # 当遍历到同层的节点时，当前遍历这个肯定更新，于是替换掉之前的。
        nearestAncestors = [dummyRoot]
        for path in lis:
            currLevel = get_level(path)
            currNode = TreeNode('/' + path[currLevel:])
            if currLevel + 1 == len(nearestAncestors):
                nearestAncestors.append(currNode)
            elif currLevel + 1 < len(nearestAncestors):
                nearestAncestors[currLevel + 1] = currNode
            nearestAncestors[currLevel].children.append(currNode)
        
        res = [0]
        def dfs(node, currTotalLen):
            if not node:
                return
            currTotalLen += len(node.val)
            res[0] = max(res[0], currTotalLen)
            for child in node.children:
                dfs(child, currTotalLen)
        dfs(dummyRoot, 0)
        return res[0] - 1
        
"""
https://leetcode-cn.com/submissions/detail/305437499/

24 / 26 个通过测试用例
状态：解答错误

输入：
"sladjf\n\tlkjlkv\n\t\tlkjlakjlert\n\t\t\tlaskjglaksjf\n\t\t\t\tlakjgfljrtlj\n\t\t\t\t\tlskajflakjsvlj\n\t\t\t\t\t\tlskgjflkjrtlrjt\n\t\t\t\t\t\t\tlkjglkjlvkjdlvkj\n\t\t\t\t\t\t\t\tlfjkglkjfljdlv\n\t\t\t\t\t\t\t\t\tlkdfjglerjtkrjkljsd.lkvjlkajlfk\n\t\t\t\t\t\t\tlskfjlksjljslvjxjlvkzjljajoiwjejlskjslfj.slkjflskjldfkjoietruioskljfkljf\n\t\t\t\t\tlkasjfljsaljlxkcjzljvl.asljlksaj\n\t\t\t\tasldjflksajf\n\t\t\t\talskjflkasjlvkja\n\t\t\t\twioeuoiwutrljsgfjlskfg\n\t\t\t\taslkjvlksjvlkjsflgj\n\t\t\t\t\tlkvnlksfgk.salfkjaslfjskljfv\n\t\t\tlksdjflsajlkfj\n\t\t\tlasjflaskjlk\n\t\tlsakjflkasjfkljas\n\t\tlskjvljvlkjlsjfkgljfg\n\tsaljkglksajvlkjvkljlkjvksdj\n\tlsakjglksajkvjlkjdklvj\n\tlskjflksjglkdjbkljdbkjslkj\n\t\tlkjglkfjkljsdflj\n\t\t\tlskjfglkjdfgkljsdflj\n\t\t\t\tlkfjglksdjlkjbsdlkjbk\n\t\t\t\t\tlkfgjlejrtljkljsdflgjl\n\t\t\t\t\tsalgkfjlksfjgkljsgfjl\n\t\t\t\t\tsalkflajwoieu\n\t\t\t\t\t\tlaskjfglsjfgljkkvjsdlkjbklds\n\t\t\t\t\t\t\tlasjglriotuojgkjsldfgjsklfgjl\n\t\t\t\t\t\t\t\tlkajglkjskljsdljblkdfjblfjlbjs\n\t\t\t\t\t\t\t\t\tlkajgljroituksfglkjslkjgoi\n\t\t\t\t\t\t\t\t\t\tlkjglkjkljkljdkbljsdfljgklfdj\n\t\t\t\t\t\t\t\t\t\t\tlkjlgkjljgslkdkldjblkj\n\t\t\t\t\t\t\t\t\t\t\t\tlkjfglkjlkjbsdklj.slgfjalksjglkfjglf\n\t\t\t\t\t\t\t\t\t\t\t\tlkasjrlkjwlrjljsl\n\t\t\t\t\t\t\t\t\t\t\t\t\tlksjgflkjfklgjljbljls\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjsglkjlkjfkljdklbjkldf\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjglkjdlsfjdglsdjgjlxljjlrjsgjsjlk\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjsgkllksjfgjljdslfkjlkasjdflkjxcljvlkjsgkljsfg\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlaskjlkjsakljglsdjfgksdjlkgjdlskjb\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkajsgfljfklgjlkdjgfklsdjklj\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjfglkjlkgjlkjl.aslkjflasjlajglkjaf\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tlkjasflgjlskjglkfjgklgsdjflkbjsdklfjskldfjgklsfdjgklfdjgl\n\tlskadjlkjsldwwwwwfj\n\t\tlkjflkasjlfjlkjajslfkjlasjkdlfjlaskjalvwwwwwwwwwwwwwwwkjlsjfglkjalsjgflkjaljlkdsjslbjsljksldjlsjdlkjljvblkjlkajfljgasljfkajgfljfjgldjblkjsdljgsldjg.skljf"
输出：
549
预期结果：
528
"""
