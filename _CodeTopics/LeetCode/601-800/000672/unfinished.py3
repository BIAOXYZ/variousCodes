class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        def compute_op(op, s):
            tmp = list(s)
            if op == 1:
                x = list(map(lambda x : '1' if x == '0' else '0', tmp))
                print(x)
            elif op == 2:
                map(lambda x : '1' if x == '0' else '0', tmp[2::2])
            elif op == 3:
                map(lambda x : '1' if x == '0' else '0', tmp[1::2])
            elif op == 4:
                map(lambda x : '1' if x == '0' else '0', tmp[1::3])
            return ''.join(tmp)

        se = set(['0'*(n+1)])
        for _ in range(presses):
            tmpSet = set()
            for s in se:
                for op in range(1, 5):
                    tmpSet.add(compute_op(op, s))
            se = tmpSet
        return len(se)
