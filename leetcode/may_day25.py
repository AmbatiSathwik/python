class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if (i != '+' and i != '-' and i != '*' and i != '/'):
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                #print(stack)
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(b-a)
                elif i == '*':
                    stack.append(a*b)
                elif i == '/':
                    stack.append(int(b/a))
        k = stack.pop()
        return k
