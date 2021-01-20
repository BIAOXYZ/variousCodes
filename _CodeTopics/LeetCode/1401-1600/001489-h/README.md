
`1489. 找到最小生成树里的关键边和伪关键边` https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/solution/zhao-dao-zui-xiao-sheng-cheng-shu-li-de-gu57q/
- > **前言**
  * > 要想解决本题，需要用到「最小生成树」以及对应求解最小生成树的「Kruskal 算法」。
  * > 对上述算法和数据结构的讲解不是本篇题解的重点，因此这里希望读者在对掌握了这些知识点之后，再来尝试解决本题。
  * > 本篇题解中会给出两种算法，并且每种算法都默认读者已经掌握了对应的知识点：
    + > 方法一只需要枚举每一条边，并用略微修改的 Kruskal 算法判断其是否是关键边或伪关键边；
    + > 方法二利用了 Kruskal 算法的连通性性质，以及无向图找桥边的 Tarjan 算法，即使在竞赛中也不算容易，仅供读者挑战自我。
- 方法一：枚举 + 最小生成树判定
- 方法二：连通性 + 最小生成树性质
