# Approach 2: Depth First Search (Trie)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class WordDictionary:

    def __init__(self):

        # Approach 1: Brute Force
        # self.s = []


        # Approach 2: Depth First Search (Trie)
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        
        # Approach 1: Brute Force
        # self.s.append(word)


        # Approach 2: Depth First Search (Trie)
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.eow = True

    def search(self, word: str) -> bool:
        
        # Approach 1: Brute Force
        # for cur in self.s:
        #     if len(word) != len(cur):
        #         continue

        #     i = 0
        #     while i < len(cur):
        #         if cur[i] == word[i] or word[i] == ".":
        #             i += 1
        #         else:
        #             break

        #     if i == len(word): return True
        # return False


        # Approach 2: Depth First Search (Trie)
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c in cur.children:
                        cur = cur.children[c]
                    else:
                        return False
            return cur.eow

        return dfs(0, self.root)