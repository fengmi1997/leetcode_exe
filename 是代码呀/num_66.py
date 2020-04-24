# num_66

class Solution:
    def plusOne(self, digits):
        i=len(digits)-1
        while i>0:
            if digits[i]+1<10:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i-=1
        if digits[i]+1<10:
                digits[i] += 1
                return digits
        else:
            digits[i] = 0
            return [1]+digits


if __name__ == '__main__':
    nums = [9,9]
    print(Solution().plusOne(nums))