class Solution {
public:
    int longestPalindrome(string s) {

        unordered_map<char, int> dic;
        for (char ch : s) {
            if (dic.find(ch) != dic.end()) {
                dic[ch]++;
            } else {
                dic[ch] = 1;
            }
        }

        int res = 0;
        bool flag = false;
        for (auto it = dic.begin(); it != dic.end(); ++it) {
            if (it->second % 2 == 0) {
                res += it->second;
            } else {
                flag = true;
                res += it->second - 1;
            }
        }

        if (!flag) {
            return res;
        } else {
            return res + 1;
        }
    }
};

/*
https://leetcode-cn.com/submissions/detail/160678279/

95 / 95 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 6.6 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：6.6 MB, 在所有 C++ 提交中击败了50.40%的用户
*/
/*
呃，感觉就是个中规中矩的实现啊，结果时间也击败百分之百了，还是零毫秒。我都有点怀疑这0ms是bug了。。。
*/
