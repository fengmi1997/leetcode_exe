class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        s = s.replace(' ','')
        i,j = 0,len(s)-1
        while i<j:
            if 'a'>s[i] or s[i]>'z':
                i+=1
                continue
            if 'a'>s[j] or s[j]>'z':
                j-=1
                continue
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False
        return True

if __name__=='__main__':
    s = "race a car"
    print(Solution().isPalindrome(s))