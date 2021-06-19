class Node():
    def __init__(self, name):
        self.name = name
        self.sons = []
        self.alive = True

class ThroneInheritance(object):
    kingNode = None
    dic = {}

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.kingNode = Node(kingName)
        self.dic[kingName] = self.kingNode

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        childNode = Node(childName)
        self.dic[childName] = childNode
        self.dic[parentName].sons.append(childNode)

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.dic[name].alive = False

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """

        res = []
        def dfs(currNode):
            if currNode.alive:
                res.append(currNode.name)
            for childNode in currNode.sons:
                dfs(childNode)
        dfs(self.kingNode)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

"""
https://leetcode-cn.com/submissions/detail/188098388/

49 / 49 个通过测试用例
状态：通过
执行用时: 1884 ms
内存消耗: 111.2 MB

执行用时：1884 ms, 在所有 Python 提交中击败了20.00%的用户
内存消耗：111.2 MB, 在所有 Python 提交中击败了20.00%的用户
"""
