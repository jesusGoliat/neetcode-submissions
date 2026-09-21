class Solution:
    def simplifyPath(self, path: str):
        new_path = [x for x in path.split('/') if x]#We don't want None values
        stack = ['/']
        for element in new_path:
            count = 0
            if stack[-1] != '/':
                stack.append('/')
            #We check if it have '..' or '.'
            if len(element) < 3:
                for c in element:
                    if c != '.':
                        count = 0 
                        break
                    count += 1
            if count == 0:
                stack.append(element)
            else:
                while len(stack) > 1 and count > 0:
                    if stack[-1] == '/':
                        count -= 1
                    stack.pop()
        return "".join(stack)
            
        