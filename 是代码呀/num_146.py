# num_146
# 这肯定不对，太复杂了
# 提交了别人的代码，主要是要想到一个有序的字典


class LRUCache:

    def __init__(self, capacity: int):
        self.pos = {}
        self.diction = {}
        self.action = [0]*capacity
        self.length = capacity

    def get(self, key: int) -> int:
        if key in self.diction:
            pos = self.pos[key]
            self.action[pos] += 1
            return self.diction[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.diction) < self.length:
            pos = len(self.diction)
            self.pos[key] = pos
            self.action[pos] += 1
            self.diction[key] = value
        else:
            # 找到待删除的pos
            pos = self.action.index(min(self.action))
            self.action = [0] * self.length
            self.action[pos] = 1
            del_key = list(self.pos.keys())[list(self.pos.values()).index(pos)]
            del self.diction[del_key]
            del self.pos[del_key]
            self.diction[key] = value
            self.pos[key] = pos


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)

