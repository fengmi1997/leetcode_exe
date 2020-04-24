# num_213
# 打家劫舍
# 动态规划，可以优化的
import json


class Solution:
    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums_1 = nums[1:]
            nums_2 = nums[0:len(nums)-1]
            dp_without1 = [0] * (len(nums) + 1)
            dp_without2 = [0] * (len(nums) + 1)
            k=2
            for i in nums_1:
                dp_without1[k] = max(dp_without1[k-1],dp_without1[k-2]+i)
                k+=1
            k=2
            for i in nums_2:
                dp_without2[k] = max(dp_without2[k-1],dp_without2[k-2]+i)
                k+=1
            return max(dp_without1[-1], dp_without2[-1])


def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            nums = [1];

            ret = Solution().rob(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()