#To check if it's a digit -> .isdigit()
class Solution:
    def decodeString(self, s: str) :
        stack = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '[':
                x = []
                k = 0
                base = 0
                while stack[-1] != ']':
                    x.append(stack.pop())
                stack.pop()
                i -= 1
                while i >= 0 and s[i].isdigit():
                    k += int(s[i])*(10**base) 
                    base += 1
                    i -= 1
                stack.append(k*("".join(x)))
            else:
                stack.append(s[i])
                i -= 1
            
        return "".join(stack[::-1])