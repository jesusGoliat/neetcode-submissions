#warmer temperature refers to nums[p] > nums[i] where p > i
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for idx,x in enumerate(temperatures):

            while stack and stack[-1][0] < x:
                _,day = stack.pop()
                result[day] = idx - day
                
            stack.append((x,idx))
            
        return result