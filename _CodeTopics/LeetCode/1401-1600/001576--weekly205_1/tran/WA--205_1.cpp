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
                    s[i-1] = 'c';
            }
        }
        return s;
    }
};

/*
https://leetcode-cn.com/submissions/detail/255048395/

775 / 776 个通过测试用例
状态：解答错误

输入：
"c?a"
输出：
"cca"
预期结果：
"cba"
*/
/*
这个就是之前对了，但是我今天看就有问题，果然确实是有问题的。
*/
