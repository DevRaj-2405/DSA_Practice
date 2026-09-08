class Solution(object):
    def evalRPN(self, tokens):
        stack=[]

        for t in tokens:
            if t== '+':
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)+int(first))

            elif t== '*':
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)*int(first))

            elif t== '/':
                first=stack.pop()
                second=stack.pop()
                stack.append(int(float(second)/float(first)))
            
            elif t== '-':
                first=stack.pop()
                second=stack.pop()
                stack.append(int(second)-int(first))

            else:
                stack.append(int(t))
        
        return stack[0]
        