# num_56
# 合并区间
# 自己写出来了，先排序，再结合栈的思想


class Solution:
    def merge(self, intervals):
        if intervals == []:
            return []
        else:
            # 现根据第一个元素进行排序,改进排序
            intervals.sort()
            # 用一个栈来完成比较
            res = [intervals[0]]
            intervals.pop(0)
            while intervals:
                if res[-1][1] >= intervals[0][0]:
                    if res[-1][1] >= intervals[0][1]:
                        res.append([res[-1][0], res[-1][1]])
                        res.pop(-2)
                    else:
                        res.append([res[-1][0], intervals[0][1]])
                        res.pop(-2)
                else:
                    res.append([intervals[0][0],intervals[0][1]])
                intervals.pop(0)
            return res


if __name__ == '__main__':
    intervals = [[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]]
    print(Solution().merge(intervals))