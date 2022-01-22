class Solution {
public:
    int removePalindromeSub(string s) {
        
        std::function<bool(string)> is_palindrome = [](string s) -> bool {
            int left = 0, right = s.size()-1;
            while (left < right) {
                if (s[left] != s[right]) {
                    return false;
                }
                ++left;
                --right;
            }
            return true;
        };

        return is_palindrome(s) ? 1 : 2;
    }
};

/*
https://leetcode-cn.com/submissions/detail/261221099/

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6 MB, 在所有 C++ 提交中击败了84.36%的用户
通过测试用例：
48 / 48
*/
