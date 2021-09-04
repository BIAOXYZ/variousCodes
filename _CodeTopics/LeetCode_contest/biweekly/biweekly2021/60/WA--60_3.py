class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        n = len(parent)
        self.locks = {i:-1 for i in range(n)}
        
        self.ancestors = {i:[] for i in range(n)}
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
https://leetcode-cn.com/submissions/detail/215248085/

14 / 150 个通过测试用例
状态：解答错误

最后执行的输入：
["LockingTree","upgrade","upgrade","upgrade","upgrade","unlock","unlock","upgrade","upgrade","upgrade","lock","lock","upgrade","upgrade","unlock","upgrade","upgrade","upgrade","upgrade","unlock","unlock"]
[[[-1,6,5,5,7,0,7,0,0,6]],[5,3],[2,3],[7,39],[1,32],[5,44],[2,15],[1,11],[1,18],[3,7],[5,36],[5,42],[8,5],[1,19],[3,38],[0,27],[4,11],[9,2],[8,41],[5,36],[7,29]]
"""
