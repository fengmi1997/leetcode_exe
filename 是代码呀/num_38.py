# num_38

class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(2,n+1):
            new_res = ''
            while res:
                j = 1
                while j<len(res) and res[j] == res[0]:
                    j += 1
                new_res += str(j)+res[0]
                res = res[j:]
            res = new_res
        return res

if __name__ =="__main__":
    n = 5
    print(Solution().countAndSay(n))