class Solution(object):
    def longestCommonPrefix(self, strs):
        size = len(strs)
        
        if size == 0:
            return " "
        if size == 1:
            return strs[0]
        
        strs.sort()
        end = min(len(strs[0]), len(strs[size - 1]))
	
        
        i = 0
    
        while(i<end and strs[0][i] == strs[size-1][i] ):
         i=i+1
        
        
        pre = strs[0][0:i]
        return pre
