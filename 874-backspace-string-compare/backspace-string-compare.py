# class Solution(object):

#     def backspaceCompare(self, s, t):
#         s1=[]
#         t1=[]
#         for i in list(s):
#             if i=='#':
              
#             elif len(s1)>0:

#                 s1.pop()

#             else:
#                 s1.append(i)
        
#         for i in list(t):
#             if i=='#':
            
#             elif len(t1)>0:
#                 t1.pop()

#             else:
#                 t1.append(i)

#         return t1==s1



class Solution(object):

    def backspaceCompare(self, s, t):
        s1=[]
        t1=[]
        for i in list(s):
            if i=='#':
                if len(s1)>0:
                    s1.pop()
            else:
                s1.append(i)

        for i in list(t):
            if i=='#':
                if len(t1)>0:
                    t1.pop()
            else:
                t1.append(i)

        return t1==s1
