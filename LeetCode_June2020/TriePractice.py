class TrieNode:
    def __init__(self):
        self.children =[None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root_node =TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root_node
        for i in range(len(word)):
            if current_node.children[ord(word[i])-97] is None:
                new_node = TrieNode()
                current_node.children[ord(word[i])-97] = new_node
            if i == len(word)-1:
                current_node.children[ord(word[i])-97].is_end = True
            current_node = current_node.children[ord(word[i])-97]

    def search(self, word: str) -> bool:
        current_node = self.root_node
        for i in range(len(word)):
            if current_node.children[ord(word[i])-97] is None:
                return False
            current_node = current_node.children[ord(word[i])-97]
        if current_node.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root_node
        for i in range(len(prefix)):
            if current_node.children[ord(prefix[i])-97] is None:
                return False
            current_node = current_node.children[ord(prefix[i])-97]
        return True



obj = Trie()
obj.insert("apple")
print(obj.search("app"))
print(obj.startsWith("app"))
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)