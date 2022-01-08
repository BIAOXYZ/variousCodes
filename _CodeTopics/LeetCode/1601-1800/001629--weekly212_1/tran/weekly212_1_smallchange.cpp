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
            // 接上文：提交试了下，确实如此，修改一下好了。。。
            if (timeList[i] > maxTime) {
                maxTime = timeList[i];
                res = keysPressed[i];
            } else if (timeList[i] == maxTime && keysPressed[i] > res) {
                res = keysPressed[i];
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/256435597/

执行用时：8 ms, 在所有 C++ 提交中击败了69.58%的用户
内存消耗：10.7 MB, 在所有 C++ 提交中击败了20.42%的用户
通过测试用例：
109 / 109
*/
