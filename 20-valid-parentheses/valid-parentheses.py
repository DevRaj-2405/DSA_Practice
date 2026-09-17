class Solution(object):
    def isValid(self, s):
        n=len(s)
        
        #Corner Case is that when the length of string is odd then it is not going to be valid parenthesis as you can see in the following step
        if n%2==1:
            return False

        st=[]

        for ch in list(s):
            #opening brackets
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)

            #closing brackets
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if ch==')' and top!='(':
                    return False

                elif ch=='}' and top!='{':
                    return False

                elif ch==']' and top!='[':
                    return False

        if len(st)==0:
            return True
        else:
            return False
    