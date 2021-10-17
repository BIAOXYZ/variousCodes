class Bank(object):

    def __init__(self, balance):
        """
        :type balance: List[int]
        """
        self.b = balance
        self.n = len(balance)
        

    def transfer(self, account1, account2, money):
        """
        :type account1: int
        :type account2: int
        :type money: int
        :rtype: bool
        """
        if account1 <= self.n and account2 <= self.n:
            if self.b[account1-1] >= money:
                self.b[account1-1] -= money
                self.b[account2-1] += money
                return True
        return False


    def deposit(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account <= self.n:
            self.b[account-1] += money
            return True
        return False


    def withdraw(self, account, money):
        """
        :type account: int
        :type money: int
        :rtype: bool
        """
        if account <= self.n and self.b[account-1] >= money:
            self.b[account-1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

"""
https://leetcode-cn.com/submissions/detail/229588078/

22 / 22 个通过测试用例
状态：通过
执行用时: 1160 ms
内存消耗: 42.6 MB
"""
