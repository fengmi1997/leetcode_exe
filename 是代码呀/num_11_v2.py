# ac
# 乘最多水的容器


class Solution(object):
    def maxArea(self, height):
        area = []
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                height_cal = height[i]
                length_cal = j-i
                s = height_cal * length_cal
                area.append(s)
                i += 1
            elif height[i] > height[j]:
                height_cal = height[j]
                length_cal = j-i
                s = height_cal * length_cal
                area.append(s)
                j -= 1
            else:
                height_cal = height[j]
                length_cal = j - i
                s = height_cal * length_cal
                area.append(s)
                i += 1
                j -= 1
        results = max(area)
        return results


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))