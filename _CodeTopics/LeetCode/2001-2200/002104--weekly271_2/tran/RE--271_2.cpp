class Solution {
public:
    long long subArrayRanges(vector<int>& nums) {

        // 第 271 场周赛第二题
        // https://leetcode-cn.com/submissions/detail/247648046/

        int n = nums.size();
        if (n == 1)
            return 0;
        
        vector<int> dp(n, 0);
        dp[0] = 0;
        dp[1] = abs(nums[1] - nums[0]);
        for (int i = 2; i < n; ++i) {
            int incr = 0;
            int currMax = nums[i], currMin = nums[i];
            for (int j = i-1; j > -1; --j) {
                currMax = max(currMax, nums[j]);
                currMin = min(currMin, nums[j]);
                incr += currMax - currMin;
            }
            dp[i] = dp[i-1] + incr;
        }
        return dp[n-1];
    }
};

/*
https://leetcode-cn.com/submissions/detail/277369813/

24 / 71 个通过测试用例
状态：执行出错

执行出错信息：
Line 23: Char 29: runtime error: signed integer overflow: 2118956545 + 28760814 cannot be represented in type 'int' (solution.cpp)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior prog_joined.cpp:32:29
最后执行的输入：
[-31372,86677,70463,37727,-91683,-41347,-90576,-82174,-84198,-5148,-12591,-34156,49770,9666,-77075,-57678,-31101,-47531,-86306,-91337,-89507,-24917,-87692,-39171,98075,17787,-42549,34352,-70752,71832,70055,-1026,3784,2190,-36669,959,50619,97129,77088,54049,51707,72052,59230,-96834,-14048,-9619,84853,99362,69885,74086,-28737,23060,-63323,13156,-72998,94336,-75409,58266,-86800,-54564,80773,40687,-47207,43609,-56556,21192,-48024,-58907,1629,-65561,-68397,31862,-2201,-34966,43542,-59201,-3637,-21936,-93559,49435,23249,-54299,70508,-90795,-3620,-33894,43927,10208,-7390,86931,48175,81859,95058,-16614,38066,-99361,63621,-99285,-47111,29933,73901,60455,46586,-84117,35256,-89853,33383,-91662,82979,-48835,-93877,-80929,-98904,-47773,69451,85183,-14449,-51496,75765,35062,12456,35254,-16363,80792,-3414,9244,62961,-52057,56344,-50277,-26870,-63323,54993,75596,-93637,-78526,-3058,-30560,82233,-50795,-5290,-641,-83040,13524,86725,23735,29280,43938,-43995,-8992,-83717,-62090,74538,58682,-56550,-8638,61528,-87974]
*/
/*
原版没问题，翻译版有问题：Python原版是没问题的，C++出现了有符号整数溢出。
*/
