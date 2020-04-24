# num_560
# 和为K的子数组

"""
用哈希表存储和出现的次数
hash_table:{sum:次数}
"""
class Solution:
    def subarraySum(self, nums, k: int) -> int:

        hash_table = {0:1}
        sum = 0
        # 用来记录sum-k出现的次数
        res = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in hash_table:
                res += hash_table[sum - k]
            if sum not in hash_table:
                hash_table[sum] = 1
            else:
                hash_table[sum] += 1
        return hash_table,res


if __name__ == '__main__':
    nums = [-1,-1,1]
    k = 1
    print(Solution().subarraySum(nums,k))