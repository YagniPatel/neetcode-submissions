class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Approach 1: Sorting

        # if len(s) != len(t):
        #     return False
        
        # return sorted(s) == sorted(t)

        # Approach 2: Hash Map

        # if len(s) != len(t):
        #     return False

        # countS, countT = defaultdict(int), defaultdict(int)

        # for i in range(len(s)):
        #     countS[s[i]] += 1
        #     countT[t[i]] += 1
        # return countS == countT

        # Approach 3: Hash Table

        if len(s) != len(t):
            return False

        count = [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for v in count:
            if v != 0:
                return False
                
        return True