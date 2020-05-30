# ac
# 四数之和,参考三数之和写的
# 1025


class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) == 0:
            results = []
        else:
            results = []
            nums.sort(reverse=False)
            k = 0
            t = len(nums) - 1
            while k < t:
                while k < t:
                    i = k + 1
                    j = t - 1
                    while i < j:
                        s = nums[k] + nums[t] + nums[i] + nums[j]
                        if s == target:
                            results.append([nums[k], nums[i], nums[j], nums[t]])
                            i += 1
                            j -= 1
                            while i < j and nums[i] == nums[i-1]:
                                i += 1
                            while i < j and nums[j] == nums[j+1]:
                                j -= 1
                        elif s < target:
                            i += 1
                            while i < j and nums[i] == nums[i-1]:
                                i += 1
                        else:
                            j -= 1
                            while i < j and nums[j] == nums[j+1]:
                                j -= 1
                    t -= 1
                    while k < t and nums[t] == nums[t + 1]:
                        t -= 1
                k += 1
                t = len(nums) - 1
                while k < t and nums[k] == nums[k - 1]:
                    k += 1
        return results


if __name__ == '__main__':
    nums = [-1,-5,-5,-3,2,5,0,4]
    target = -7
    print(Solution().fourSum(nums, target))