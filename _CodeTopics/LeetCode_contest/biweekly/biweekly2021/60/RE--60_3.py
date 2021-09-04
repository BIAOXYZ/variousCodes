class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        n = len(parent)
        self.locks = {i:-1 for i in range(n)}
        
        self.ancestors = {0:[]}
        for i in range(1, n):
            father = parent[i]
            self.ancestors[i] = [father] + self.ancestors[father]
        
        self.descendants = {i:[] for i in range(n)}
        for i in range(n-1, 0, -1):
            curr = parent[i]
            self.descendants[curr] = self.descendants[curr] + [i] + self.descendants[i]
        
        ##print self.descendants
        ##print self.ancestors


    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locks[num] == -1:
            self.locks[num] = user
            return True
        return False


    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if self.locks[num] == user:
            self.locks[num] = -1
            return True
        return False

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        flag1 = True
        if self.locks[num] != -1:
            flag1 = False
        flag2 = False
        for i in self.descendants[num]:
            if self.locks[i] != -1:
                flag2 = True
                break
        flag3 = True
        for i in self.ancestors[num]:
            if self.locks[i] == -1:
                flag3 = False
                break
        flag = flag1 and flag2 and flag3
        if flag:
            self.locks[num] = user
            for i in self.descendants[num]:
                self.locks[i] == -1
            return True
        return False
    

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

"""
https://leetcode-cn.com/submissions/detail/215239770/

1 / 150 个通过测试用例
状态：执行出错

执行出错信息：
KeyError: 3
    self.ancestors[i] = [father] + self.ancestors[father]
Line 13 in __init__ (Solution.py)
    obj = LockingTree(__Deserializer__()._deserialize(json.dumps(cargs[0], separators=(",", ":")), "integer[]"))
Line 139 in _driver (Solution.py)
    _driver()
Line 153 in <module> (Solution.py)
最后执行的输入：
["LockingTree","upgrade","upgrade","unlock","lock","upgrade"]
[[[-1,0,3,1,0]],[4,5],[3,8],[0,7],[2,7],[4,6]]
"""
