class Solution(object):
    def maxAbsoluteSum(self, nums):
        res=0
        pos=0
        neg=0

        for n in nums:
            pos+=n
            if pos < 0:
                pos=0
            neg+=n
            if neg > 0:
                neg=0
            
            res=max(res,pos,abs(neg))
        return res
        