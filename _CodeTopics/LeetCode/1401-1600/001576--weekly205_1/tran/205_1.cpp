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
                if (s[i] == s[i-1]) {
                    if (i > 1) {
                        if (s[i-2] != 'a' && s[i] != 'a')
                            s[i-1] = 'a';
                        else if (s[i-2] != 'b' && s[i] != 'b')
                            s[i-1] = 'b';
                        else
                            s[i-1] = 'c';
                    } else {
                        s[i-1] = 'b';
                    }
                }
            }
        }
        return s;
    }
};

/*
https://leetcode-cn.com/submissions/detail/255050207/

执行用时：4 ms, 在所有 C++ 提交中击败了43.75%的用户
内存消耗：5.9 MB, 在所有 C++ 提交中击败了67.97%的用户
通过测试用例：
776 / 776
*/
