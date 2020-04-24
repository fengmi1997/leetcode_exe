# num_347
# 用排序字典写的


import collections
class Solution:
    def topKFrequent(self, nums, k: int):
        res = []
        # 用字典存储出现的频率
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        kd = collections.OrderedDict(sorted(dic.items(),key=lambda x:x[1],reverse=True))
        for key in kd.keys():
            if len(res)<k:
                res.append(key)
            else:
                break
        return res



if __name__=='__main__':
    nums = [-1,-1]
    k=1
    print(Solution().topKFrequent(nums,k))
