// 不知道为啥 "1"、"11"、"111"都对，但是四个或以上的1组成的串就不行了。。。
// 我就是按python版本翻译的啊。不管了，留着`TODO`了。。。
class Solution {
public:
    int is_legal_encode(string s) {
        if (s[0] == '0' || stoi(s) > 26) {
            return 0;
        } else {
            return 1;
        }
    }

    int numDecodings(string s) {
        int length = s.size();
        vector<int> dp(length, 0);

        for (int i = 0; i < length; ++i) {
            if (i == 0)
                dp[i] = is_legal_encode(s.substr(i,i+1));
            else if (i == 1)
                dp[i] = dp[i-1]*is_legal_encode(s.substr(i,i+1)) + is_legal_encode(s.substr(i-1,i+1));
            else
                dp[i] = dp[i-1]*is_legal_encode(s.substr(i,i+1)) + dp[i-2]*is_legal_encode(s.substr(i-1,i+1));
        }
        return dp[length-1];
    }
};

/*
https://leetcode-cn.com/submissions/detail/170242764/

16 / 269 个通过测试用例
状态：解答错误

输入：
"2101"
输出：
0
预期：
1
*/
