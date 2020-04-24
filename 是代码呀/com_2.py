class Solution:
    def getTriggerTime(self, increase, requirements) :
        # # 把requirements排序
        # b = sorted(enumerate(requirements), key=lambda x: x[1])
        # force = [0, 0, 0]
        # res = [-1] * len(requirements)
        # for day in range(len(increase)):
        #     for resource in range(len(increase[0])):
        #         force[resource] += increase[day][resource]
        #     for i in range(len(b)):
        #         re = b[i][1]
        #         if force[0] >= re[0] and force[1] >= re[1] and force[2] >= re[2]:
        #             res[day] = day
        #             break
        # return res
        # 把requirements排序
        '''
        force = [0, 0, 0]
        res = [-1] * len(requirements)
        for i in range(len(requirements)):
            if force[0] >= requirements[i][0] and force[1] >= requirements[i][1] and force[2] >= requirements[i][2]:
                res[i] = 0
        for day in range(len(increase)):
            force=[i+j for i,j in zip(force,increase[day])]
            # for resource in range(len(increase[0])):
            #     force[resource] += increase[day][resource]
            for i in range(len(requirements)):
                if force[0] >= requirements[i][0] and force[1] >= requirements[i][1] and force[2] >= requirements[i][2]:
                    if res[i] == -1:
                        res[i] = day+1
        return res
        '''
        forces = [[0,0,0]]
        res = [-1] * len(requirements)
        for day in range(len(increase)):
            forces.append([i + j for i, j in zip(forces[-1], increase[day])])
        for i,requirement in enumerate(requirements):
            left, right=0, len(forces)-1
            while left<=right:
                mid=left+(right-left)//2
                if requirement[0]<=forces[mid][0] and requirement[1]<=forces[mid][1] and requirement[2]<=forces[mid][2]:
                    res[i] = mid
                    right=mid-1
                else:
                    left=mid+1
        return res



# increase =[[2,8,4],[2,5,0],[10,9,8]]
# requirements =[[2,11,3],[15,10,7],[9,17,12],[8,1,14]]
increase =[[0,4,5],[4,8,8],[8,6,1],[10,10,0]]
requirements =[[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]
# increase =[[1,1,1]]
# requirements =[[0,0,0]]


print(Solution().getTriggerTime(increase,requirements))