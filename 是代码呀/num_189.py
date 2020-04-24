class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        超时了
        """
        # while k!=0:
        #     n = nums[len(nums)-1]
        #     for i in range(len(nums)-1,0,-1):
        #         nums[i]=nums[i-1]
        #     nums[0] = n
        #     k-=1
        # return nums
        """
        这个空间复杂度有是n
        """
        if k>len(nums):
            k = k%(len(nums))
        n = nums[-k:]
        pos = -1
        for i in range(len(nums)-k-1,-1,-1):
            nums[pos] = nums[i]
            pos-=1
        for i in range(k):
            nums[i] = n[i]
        return nums,n

if __name__=='__main__':
    nums = [1,2]
    print(Solution().rotate(nums,k=3))