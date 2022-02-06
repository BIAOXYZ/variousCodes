// 怕 Python 字符串操作会超时，第一次比赛里用了 C++。但是我估计这个trivial的写法
// 还是会超时的，主要就在 flip 那里。正确的做法应该是记住 flip 的次数。
// --> 改用记录 flip 次数（其实只记录奇偶性即可）的写法。

class Bitset {
public:
    int size;
    string s;
    int cnt;
    int flipFlag;
public:
    void realflip() {
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

public:
    Bitset(int size) {
        this->size = size;
        this->s = string(size, '0');
        this->cnt = 0;
        this->flipFlag = 0;
    }
    
    void fix(int idx) {
        if (!this->flipFlag && this->s[idx] == '0') {
            ++this->cnt;
            this->s[idx] = '1';
        }
        if (this->flipFlag && this->s[idx] == '1') {
            --this->cnt;
            this->s[idx] = '0';
        }    
    }
    
    void unfix(int idx) {
        if (!this->flipFlag && this->s[idx] == '1') {
            --this->cnt;
            this->s[idx] = '0';
        }
        if (this->flipFlag && this->s[idx] == '0') {
            ++this->cnt;
            this->s[idx] = '1';
        }
    }
    
    void flip() {
        this->flipFlag ^= 1; 
    }
    
    bool all() {
        if (!this->flipFlag)
            return this->cnt == this->size ? true : false;
        else
            return this->cnt == 0 ? true : false;
    }
    
    bool one() {
        if (!this->flipFlag)
            return this->cnt != 0 ? true : false;
        else
            return this->cnt != this->size ? true : false;
    }
    
    int count() {
        return this->flipFlag? this->size - this->cnt : this->cnt;
    }
    
    string toString() {
        if (this->flipFlag) {
            this->realflip();
            this->flipFlag = 0;
            this->cnt = this->size - this->cnt;
        }
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
https://leetcode-cn.com/submissions/detail/265128569/

23 / 48 个通过测试用例
状态：解答错误

输入：
["Bitset","count","flip","toString","toString","flip","all","all","count","all","count","all","unfix","unfix","unfix","count","flip","all","flip","fix","fix"]
[[1],[],[],[],[],[],[],[],[],[],[],[],[0],[0],[0],[],[],[],[],[0],[0]]
输出：
[null,0,null,"1","1",null,true,true,1,true,1,true,null,null,null,1,null,false,null,null,null]
预期：
[null,0,null,"1","1",null,false,false,0,false,0,false,null,null,null,0,null,true,null,null,null]
*/
