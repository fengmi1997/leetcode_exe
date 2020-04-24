
import json
class Solution:
    def majorityElement(self, nums) -> int:
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1
        res = []
        for key,value in zip(dic.keys(),dic.values()):
            if value > (len(nums) /2):
                res.append(key)
        return res

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

            nums = [3,2,3];

            ret = Solution().majorityElement(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()