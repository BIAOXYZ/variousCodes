
# 残余代码

```py
class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """

        if not sentence:
            return 0
        length = len(sentence)
        if not dictionary:
            return length

        maxWordLen = 0
        for word in dictionary:
            maxWordLen = max(maxWordLen, len(word))
        
        q = [i for i in range(1,length+1)]
        maxUnMatchLen = 0

        for start in range(length):
            for end in range(start+1,min(start+1+maxWordLen, length)):
                matchflag = False
                print sentence[start:end]
                if sentence[start:end] in dictionary:
                    matchflag = True
                    q[end] = q[start]
                    print "changed q is:\n", q
                print list(sentence)
                print q
                if matchflag == True:
                    """
                    if end < length - 1:
                        q[end] = q[start] + maxWordLen
                    elif end == length - 1:
                        q[length-1] = q[start] + end - start + 1
                    else:
                        print "This branch is just for logic clearance, it cannot happen."
                    """
                    for i in range(end+1, length):
                        q[i] = min(q[i], q[end]+i-end)
        return q[-1]
```
