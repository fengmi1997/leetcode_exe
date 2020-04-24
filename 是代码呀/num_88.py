class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0
        for num in nums2:
            if 0 in nums1:
                for j in range(len(nums1) - 1, -1, -1):
                    if nums1[j] != 0:
                        pos_0 = j + 1
                        break
                    if j == 0:
                        pos_0 = 0
            for i in range(start, len(nums1)):
                # 用i来记录此时要插入的位置，用j记录0开始的位置，每次删掉j所在的位置
                if (nums1[i - 1] <= num and num < nums1[i]) or (num < nums1[i]):
                    for j in range(pos_0, i, -1):
                        nums1[j] = nums1[j - 1]
                    nums1[i] = num
                    start = i + 1
                    break

                if i>=pos_0 and nums1[i] == 0 and num >= nums1[i - 1]:
                    nums1[i] = num
                    start = i + 1
                    break


import json
def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line);
            line = next(lines)
            m = int(line);
            line = next(lines)
            nums2 = stringToIntegerList(line);
            line = next(lines)
            n = int(line);

            ret = Solution().merge(nums1, m, nums2, n)

            out = integerListToString(nums1)
            if ret is not None:
                print("Do not return anything, modify nums1 in-place instead.")
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()