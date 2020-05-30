# 超时未通过
# 乘最多水的容器


class Solution(object):
    def maxArea(self, height):
        results = []
        area = []
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                height_cal = min(height[i], height[j])
                length_cal = j-i
                s = height_cal * length_cal
                area.append(s)
        results = max(area)
        return results


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))