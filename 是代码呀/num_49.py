# num_49
# 字母异位词分组
# 用哈希表，key是无顺序的字符串


class Solution:
    def groupAnagrams(self, strs):
        hash_table = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key not in hash_table:
                hash_table[key] = [str]
            else:
                hash_table[key] += [str]
        return list(hash_table.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))