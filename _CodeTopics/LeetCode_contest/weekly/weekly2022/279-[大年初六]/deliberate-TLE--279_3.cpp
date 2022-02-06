// 怕 Python 字符串操作会超时，第一次比赛里用了 C++。但是我估计这个trivial的写法
// 还是会超时的，主要就在 flip 那里。正确的做法应该是记住 flip 的次数。

class Bitset {
public:
    int size;
    string s;
    int cnt;
public:
    Bitset(int size) {
        this->size = size;
        this->s = string(size, '0');
        this->cnt = 0;
    }
    
    void fix(int idx) {
        if (this->s[idx] == '0') {
            ++this->cnt;
            this->s[idx] = '1';
        }
    }
    
    void unfix(int idx) {
        if (this->s[idx] == '1') {
            --this->cnt;
            this->s[idx] = '0';
        }
    }
    
    void flip() {
        for (int idx = 0; idx < this->size; ++idx) {
            if (this->s[idx] == '0') {
                ++this->cnt;
                this->s[idx] = '1';
            } else {
                --this->cnt;
                this->s[idx] = '0';
            }   
        }
    }
    
    bool all() {
        return this->cnt == this->size ? true : false;
    }
    
    bool one() {
        return this->cnt != 0 ? true : false;  
    }
    
    int count() {
        return this->cnt;
    }
    
    string toString() {
        return this->s;
    }
};


/**
 * Your Bitset object will be instantiated and called as such:
 * Bitset* obj = new Bitset(size);
 * obj->fix(idx);
 * obj->unfix(idx);
 * obj->flip();
 * bool param_4 = obj->all();
 * bool param_5 = obj->one();
 * int param_6 = obj->count();
 * string param_7 = obj->toString();
 */

/*
https://leetcode-cn.com/submissions/detail/265117902/

44 / 48 个通过测试用例
状态：超出时间限制

最后执行的输入：
Hidden for this testcase during contest.
标准输出：
Hidden for this testcase during contest.
*/
