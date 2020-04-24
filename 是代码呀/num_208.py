# num_208

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.stack.append(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.stack:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.stack:
            if prefix == i[:len(prefix)]:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith(prefix)

trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # 返回 true
print(trie.search("app"))    # 返回 false
print(trie.startsWith("app"))  # 返回 true
trie.insert("app")
print(trie.search("app"))  # 返回 true
print(trie.startsWith("app"))
