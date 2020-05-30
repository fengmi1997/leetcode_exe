# ac
# 三数之和,，参考别人的思路做的
# 1025


class Solution(object):
    def threeSum(self, nums):
        nums.sort(reverse=False)
        if len(nums) == 0:
            results = []
        else:
            results = []
            k = 0
            while k < len(nums) and nums[k] <= 0:
                i = k+1
                j = len(nums)-1
                while i < j:
                    s = nums[k] + nums[i] + nums[j]
                    if s == 0:
                        results.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
                    elif s < 0:
                        i += 1
                        while i < j and nums[i] == nums[i-1]:
                            i += 1
                    else:
                        j -= 1
                        while i < j and nums[j] == nums[j+1]:
                            j -= 1
                k += 1
                while k < len(nums) and nums[k] == nums[k-1]:
                    k += 1

        return results


if __name__ == '__main__':
#   nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
#   nums = [0,0,0, 0]
    nums = [0,0,0]
    print(Solution().threeSum(nums))