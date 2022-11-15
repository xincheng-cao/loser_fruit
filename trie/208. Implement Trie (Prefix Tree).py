class Trie:

    def __init__(self):
        self.children=[None]*26
        self.is_end=False

    def insert(self, word: str) -> None:
        cur_node=self
        for ch in word:
            pos=ord(ch)-ord('a')
            if cur_node.children[pos] is None:
                cur_node.children[pos]=Trie()
            cur_node=cur_node.children[pos]
        cur_node.is_end=True

    def search(self, word: str) -> bool:
        cur_node=self
        for ch in word:
            pos=ord(ch)-ord('a')
            if cur_node.children[pos] is not None:
                cur_node=cur_node.children[pos]
            else:
                return False
        if cur_node.is_end:
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        cur_node=self
        for ch in prefix:
            pos=ord(ch)-ord('a')
            if cur_node.children[pos] is not None:
                cur_node=cur_node.children[pos]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)