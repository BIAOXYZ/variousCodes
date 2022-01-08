class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {

        // 第 212 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/118405497/

        int length = releaseTimes.size();
        // 其实没必要搞这个数组，不过就是为了翻译 python 版，就还是申请了。
        vector<int> timeList = vector<int>(releaseTimes.begin(), releaseTimes.end());

        int maxTime = timeList[0];
        char res = keysPressed[0];
        for (int i = length-1; i > 0; --i) {
            timeList[i] -= timeList[i-1];
            // 我感觉这里没有考虑时间相等，但是字母顺序更大的情况啊，当时怎么过了。。。
            // 比如第一个用例变成 [9,29,49,50] "cycd" 就过不了了。。。
            if (timeList[i] > maxTime) {
                maxTime = timeList[i];
                res = keysPressed[i];
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/256435055/

102 / 109 个通过测试用例
状态：解答错误

输入：
[9,12,14,18,31,44]
"diwoha"
输出：
"a"
预期结果：
"h"
*/
