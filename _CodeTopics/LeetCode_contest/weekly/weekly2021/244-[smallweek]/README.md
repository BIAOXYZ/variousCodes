
# 中国时间：2021-06-06 10:30

第 244 场周赛 https://leetcode-cn.com/contest/weekly-contest-244
- 5776. 判断矩阵经轮转后是否一致 https://leetcode-cn.com/contest/weekly-contest-244/problems/determine-whether-matrix-can-be-obtained-by-rotation/
- 5777. 使数组元素相等的减少操作次数 https://leetcode-cn.com/contest/weekly-contest-244/problems/reduction-operations-to-make-the-array-elements-equal/
- 5778. 使二进制字符串字符交替的最少反转次数 https://leetcode-cn.com/contest/weekly-contest-244/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
- 5779. 装包裹的最小浪费空间 https://leetcode-cn.com/contest/weekly-contest-244/problems/minimum-space-wasted-from-packaging/

# (1)

第一题想玩花也是想省事，结果就发现了神奇的事情：申请二维数组的列表推导式，两种形式申请完打印的结果都对。但是常用的那种 `mat1 = [[2 for _ in range(n)] for _ in range(n)]` 没问题，今天想着试试看那种简单的形式（`mat1 = [[2]*n]*n`）行不（之前顶多用过内层用简单形式，外层用完整形式，也就是 `[[2] * n for i in range(n)]` 这种）。结果直接裂开了，不知道为啥后面明明只更新了矩阵的一个元素，但是两个元素都跟着变。。。留个`TODO`回头看看吧。

另外这个题感觉可以当模版题。矩阵旋转的时候，第一个转完，后面（还是以最初始矩阵为出发点的话）再推有点复杂，于是取了个巧：让第二次旋转的结果矩阵 mat2 以 mat1 为基准（一般更自然的想法是仍旧以最初始的矩阵 mat 为基准），同理，mat3 以 mat2 为基准。这样的好处是代码简单，因为每次旋转的逻辑是一样的；坏处是不能在单次循环里把三个矩阵都改了——不过反正第一题，矩阵维数最高就10，无所谓了。
