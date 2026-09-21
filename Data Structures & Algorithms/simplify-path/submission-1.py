class Solution:
    def simplifyPath(self, path: str):
        new_path = [x for x in path.split('/') if x]#We don't want None values
        stack = ['/']
        for element in new_path:
            if stack[-1] != '/':
                stack.append('/')
            #We check if it have '..' or '.'
            if element == ".." or element == ".":
                count = len(element)
                while len(stack) > 1 and count > 0:
                    if stack[-1] == '/':
                        count -= 1
                    stack.pop()
            else:
                stack.append(element)
     
        return "".join(stack)
            
        