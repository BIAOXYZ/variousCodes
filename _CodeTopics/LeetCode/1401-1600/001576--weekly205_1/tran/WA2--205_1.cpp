class Solution {
public:
    string modifyString(string s) {
        
        // 第 205 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/105224224/

        int length = s.size();
        if (s[0] == '?')
            s[0] = 'a';
        for (int i = 1; i < length; ++i) {
            if (s[i] == '?') {
                if (s[i-1] != 'a')
                    s[i] = 'a';
                else
                    s[i] = 'b';
            } else {
                if (s[i] == s[i-1]) 
                    if (s[i-1] == 'a')
                        s[i] = 'b';
                    else
                        s[i] = 'a';
            }
        }
        return s;
    }
};

/*
https://leetcode-cn.com/submissions/detail/255049329/

739 / 776 个通过测试用例
状态：解答错误

输入：
"j?qg??b"
输出：
"jaqgaba"
预期结果：
"jaqgacb"
*/
/*
艹，烦了，没注意题目说的不能改非问号字符。
*/
