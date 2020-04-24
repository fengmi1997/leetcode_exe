class Solution:
    def minJump(self, jump) -> int:
        pos = 0
        num = 0
        while pos<len(jump):
            if pos == 0:
                pos += jump[0]
                num+=1
            else:
                max_jump=max(jump[0:pos])
                index=jump[0:pos].index(max_jump)
                if max_jump>jump[pos]:
                    pos=index
                    num+=1
                else:
                    pos+=jump[pos]
                    num+=1
        return num


jump=[2, 5, 1, 1, 1, 1]
print(Solution().minJump(jump))