# num_621
# 任务调度器

# 贪心，官方题解第一种思路,累死了，终于通过了
class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        res = []
        hash_map = {}
        for i in range(len(tasks)):
            if tasks[i] not in hash_map:
                hash_map[tasks[i]] = 1
            else:
                hash_map[tasks[i]] += 1
        while tasks:
            one_res = []
            task = max(hash_map, key=hash_map.get)
            one_hash_map = hash_map.copy()

            for i in range(n+1):
                if tasks == []:
                    break
                if (task not in one_res) and (one_hash_map[task] != 0):
                    one_res.append(task)
                    hash_map[task] -= 1
                    tasks.remove(task)
                    del one_hash_map[task]
                    if one_hash_map == {}:
                        continue
                    else:
                        task = max(one_hash_map, key=one_hash_map.get)
                else:
                    one_res.append(None)
            res += one_res
        return len(res)


if __name__ == '__main__':
    tasks = ["A","A","A","B","B","B"]
    n = 2
    print(Solution().leastInterval(tasks, n))