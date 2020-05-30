# 未通过
# 三数之和,超时啦
class Solution(object):
    def threeSum(self, nums):
        results = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i], nums[j], nums[k]])
        tmp = []
        for i in range(len(results)):
            for j in range(i+1, len(results)):
                if results[j][0] in results[i]:
                    a = results[i].index(results[j][0])
                if results[j][1] in results[i]:
                    b = results[i].index(results[j][1])
                if results[j][2] in results[i]:
                    c = results[i].index(results[j][2])
                if results[j][0] in results[i] and results[j][1] in results[i] and results[j][2] in results[i]:
                    if a == b == c and results[i][0]+results[i][1]+results[i][1] == 0:
                        tmp.append(j)
                    if a != b or a != c or c != b:
                        tmp.append(j)
            tmp = list(set(tmp))
            tmp.sort(reverse=True)

        for i in tmp:
            results.pop(i)
        return results


if __name__ == '__main__':
#   nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    nums = []
#   nums = [3, 0, 3, 2, -4, 0, -3, 2, 2, 0, -1, -5]
    print(Solution().threeSum(nums))