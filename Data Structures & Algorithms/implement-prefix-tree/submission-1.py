# Approach 1: Prefix Tree (Array)
# class TrieNode:
#     def __init__(self):
#         self.children = [None]*26
#         self.endOfWord = False    


# Approach 2: Prefix Tree (Hash Map)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class PrefixTree:

    def __init__(self):

        # Approach 1: Prefix Tree (Array)
        # self.root = TrieNode()        


        # Approach 2: Prefix Tree (Hash Map)
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        # Approach 1: Prefix Tree (Array)
        # cur = self.root
        # for c in word:
        #     i = ord(c) - ord("a")
        #     if cur.children[i] == None:
        #         cur.children[i] = TrieNode()
        #     cur = cur.children[i]
        # cur.endOfWord = True


        # Approach 2: Prefix Tree (Hash Map)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        # Approach 1: Prefix Tree (Array)
        # cur = self.root
        # for c in word:
        #     i = ord(c) - ord("a")
        #     if cur.children[i] == None:
        #         return False
        #     cur = cur.children[i]
        # return cur.endOfWord


        # Approach 2: Prefix Tree (Hash Map)
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        
        # Approach 1: Prefix Tree (Array)
        # cur = self.root
        # for c in prefix:
        #     i = ord(c) - ord("a")
        #     if cur.children[i] == None:
        #         return False
        #     cur = cur.children[i]
        # return True        


        # Approach 2: Prefix Tree (Hash Map)
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True