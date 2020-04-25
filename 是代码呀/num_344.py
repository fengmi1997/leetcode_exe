class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        '''
        def repeat(s):
            nums=s[len(s)-1]
            for i in range(len(s)-1,0,-1):
                s[i]=s[i-1]
            s[0]=nums
            return s
        for i in range(len(s)):
            s = s[:i]+repeat(s[i:])
        '''

        i,j = 0,len(s)-1
        while i<j:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
            
