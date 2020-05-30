# ac
# 最接近的三数之和
# 自己写的


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort(reverse=False)
        k = 0
        i = 1
        j = len(nums) - 1
        results = nums[0] + nums[1] + nums[2]
        while k < len(nums):
            while i < j:
                sum = nums[k] + nums[i] + nums[j]
                if sum < target:
                    if abs(sum - target) < abs(results - target):
                        i += 1
                        results = sum
                    else:
                        i += 1
                elif sum > target:
                    if abs(sum - target) < abs(results - target):
                        j -= 1
                        results = sum
                    else:
                        j -= 1
                elif sum == target:
                    results = sum
                    return results
            k += 1
            i = k + 1
            j = len(nums) - 1
        return results


if __name__ == '__main__':
    nums = [1,2,4,8,16,32,64,128]
    target = 82
    print(Solution().threeSumClosest(nums, target))