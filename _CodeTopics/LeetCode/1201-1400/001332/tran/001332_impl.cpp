class Solution {
public:
    int removePalindromeSub(string s) {
        
        std::function<bool(string)> is_palindrome_v2 = [](string s) -> bool {
            int n = s.size();
            for (int i = 0; i < n/2; ++i) {
                if (s[i] != s[n-1-i]) {
                    return false;
                }
            }
            return true;
        };
        
        return is_palindrome_v2(s) ? 1 : 2;
    }
};

/*
https://leetcode-cn.com/submissions/detail/261288469/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6 MB, 在所有 C++ 提交中击败了65.43%的用户
通过测试用例：
48 / 48
*/
