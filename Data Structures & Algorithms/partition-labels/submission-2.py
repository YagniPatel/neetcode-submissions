class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # Approach 1: Two Pointers (Greedy)

        lastInd = defaultdict(int)
        for i, c in enumerate(s):
            lastInd[c] = i

        size = end = 0
        res = []
        for i, c in enumerate(s):
            size += 1
            end = max(end, lastInd[c])

            if i == end:
                res.append(size)
                size = 0

        return res