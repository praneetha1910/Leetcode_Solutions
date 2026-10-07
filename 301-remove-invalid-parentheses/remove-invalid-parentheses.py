class Solution:
    def removeInvalidParentheses(self, s):
        ans = [] 
        def is_valid(x):
            count = 0  
            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False

            return count == 0
        def backtrack(index, path, left, right):
            if index == len(s):
                if left == 0 and right == 0 and is_valid(path):
                    ans.append(path)
                return   
            ch = s[index]
            
            if ch == '(' and left > 0:
                backtrack(index + 1, path, left - 1, right)
            
            elif ch == ')' and right > 0:
                backtrack(index + 1, path, left, right - 1)
            
            backtrack(index + 1, path + ch, left, right)
        
        left = right = 0
        
        for ch in s:
            if ch == '(':
                left += 1
            elif ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        
        backtrack(0, "", left, right)
        
        return list(set(ans))