class Solution {
public:
    bool isAdditiveNumber(string num) {

        int length = num.size();
        if (length < 3)
            return false;
        bool res = false;

        std::function<void(int, vector<string>)> backtrack;
        backtrack = [&](int pos, vector<string> currArr) -> void {
            int currLen = currArr.size();
            if (pos == length) {
                if (currLen >= 3)
                    res = true;
                return;
            }
            if (num[pos] == '0') {
                if (currLen < 2 || (currLen >= 2 && currArr[currLen-1] == "0" && currArr[currLen-2] == "0")) {
                    currArr.push_back("0");
                    backtrack(pos+1, currArr);
                    currArr.pop_back();
                }
                return;
            }
            for (int nextPos = pos+1; nextPos < length+1; ++nextPos) {
                // 注意 substr 的第二个参数不是切片末尾，而是一共取多少个字符。。。
                string nextS = num.substr(pos, nextPos - pos);
                if (currLen < 2) {
                    currArr.push_back(nextS);
                    backtrack(nextPos, currArr);
                    currArr.pop_back();                    
                } else {
                    if (stol(nextS, nullptr, 10) == stol(currArr[currLen-1], nullptr, 10) + stol(currArr[currLen-2], nullptr, 10)) {
                    currArr.push_back(nextS);
                    backtrack(nextPos, currArr);
                    currArr.pop_back();                           
                    }
                }
            }
        };
        
        backtrack(0, vector<string>{});
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/256781193/

40 / 42 个通过测试用例
状态：执行出错

执行出错信息：
terminate called after throwing an instance of 'std::out_of_range'
  what():  stol
最后执行的输入：
"11111111111011111111111"
*/
