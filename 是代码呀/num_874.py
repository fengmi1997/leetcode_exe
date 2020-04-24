class Solution:
    def robotSim(self, commands, obstacles) -> int:
        # 首先要设置机器人的前进方向
        direction = 0
        pos = (0,0)
        dic = {0: {-2: 1, -1: 3}, 1: {-2: 2, -1: 0}, 2: {-2: 3, -1: 1}, 3: {-2: 0, -1: 2}}

        obstacleSet = set(map(tuple, obstacles))


        def new_pos(pos, num, direction):
            if direction == 0:
                for step in range(1, num + 1):
                    new = (pos[0],pos[1]+step)
                    if new in obstacleSet:
                        new = (pos[0], pos[1] + step-1)
                        break
            elif direction == 1:
                for step in range(1, num + 1):
                    new = (pos[0]-step, pos[1])
                    if new in obstacleSet:
                        new = (pos[0] - step+1, pos[1])
                        break
            elif direction == 2:
                for step in range(1, num + 1):
                    new = (pos[0], pos[1] - step)
                    if new in obstacleSet:
                        new = (pos[0], pos[1] - step+1)
                        break
            else:
                for step in range(1, num + 1):
                    new = (pos[0]+step, pos[1])
                    if new in obstacleSet:
                        new = (pos[0] + step-1, pos[1])
                        break
            return new

        res = 0
        for command in commands:
            if command > 0:
                pos = new_pos(pos, command, direction)
                res = max(res, pos[0] * pos[0] + pos[1] * pos[1])
            else:
                direction = dic[direction][command]
        return res


if __name__=='__main__':
    commands =[4, -1, 4, -2, 4]
    ocst = [[2, 4],[2,4]]
    print(Solution().robotSim(commands,ocst))