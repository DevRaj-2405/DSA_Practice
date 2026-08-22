class Solution(object):
    def backspaceCompare(self, s, t):
        s1=[]
        t1=[]
        for ch in list(s):
            if ch!='#':
                s1.append(ch)
            elif len(s1)>0:
                s1.pop()
        for ch in list(t):
            if ch!='#':
                t1.append(ch)

            elif len(t1)>0:
                t1.pop()

        return t1==s1


            