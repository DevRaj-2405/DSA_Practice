class Solution(object):
    def reverseString(self, s):
        s.reverse()
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
      

        # another method to reverse
        # i=0
        # j=len(s)-1
        # while i<j:
        #     temp=s[i]
        #     s[i]=s[j]
        #     s[j]=temp 
        #     i+=1
        #     j-=1