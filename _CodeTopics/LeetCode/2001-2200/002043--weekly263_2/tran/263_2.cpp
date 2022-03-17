class Bank {
    // 第 263 场周赛第二题
    // https://leetcode-cn.com/submissions/detail/229588078/
private:
    vector<long long> _b;
    long long _n;
public:
    Bank(vector<long long>& balance) {
        _b = balance;
        _n = balance.size();
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1 <= _n && account2 <= _n && _b[account1-1] >= money) {
            _b[account1-1] -= money;
            _b[account2-1] += money;
            return true;
        }
        return false;
    }
    
    bool deposit(int account, long long money) {
        if (account <= _n) {
            _b[account-1] += money;
            return true;
        }
        return false;
    }
    
    bool withdraw(int account, long long money) {
        if (account <= _n && _b[account-1] >= money) {
            _b[account-1] -= money;
            return true;
        }
        return false;
    }
};


/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */

/*
https://leetcode-cn.com/submissions/detail/285050281/

执行用时：196 ms, 在所有 C++ 提交中击败了93.08%的用户
内存消耗：114.2 MB, 在所有 C++ 提交中击败了33.72%的用户
通过测试用例：
23 / 23
*/
