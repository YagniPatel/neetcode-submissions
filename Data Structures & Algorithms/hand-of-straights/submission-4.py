class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # Approach 1: Sorting

        # if len(hand) % groupSize != 0: return False

        # mp = defaultdict(int)
        # for card in hand:
        #     mp[card] += 1

        # hand.sort()
        # for card in hand:
        #     if mp[card] == 0:
        #         continue

        #     for i in range(card, card + groupSize):
        #         if mp[i] <= 0:
        #             return False
        #         mp[i] -= 1

        # return True


        # Approach 2: Heap

        # if len(hand) % groupSize: return False

        # mp = defaultdict(int)
        # for card in hand:
        #     mp[card] += 1
        
        # minH = list(mp.keys())
        # heapq.heapify(minH)
        # while minH:
        #     card = minH[0]
        #     for i in range(card, card + groupSize):
        #         if mp[i] <= 0:
        #             return False
        #         mp[i] -= 1

        #         if mp[i] == 0:
        #             if i != minH[0]:
        #                 return False
        #             heapq.heappop(minH)

        # return True


        # Approach 3: Ordered Map

        # if len(hand) % groupSize != 0: return False

        # q = deque()
        # count = Counter(hand)
        # openGroup, lastNum = 0, -1

        # for num in sorted(count):
        #     if ((openGroup > 0 and num > lastNum + 1) or openGroup > count[num]):
        #         return False

        #     q.append(count[num] - openGroup)
        #     lastNum = num
        #     openGroup = count[num]

        #     if len(q) == groupSize:
        #         openGroup -= q.popleft()

        # return openGroup == 0


        # Approach 4: Hash Map

        if len(hand) % groupSize: return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1] > 0:
                start -= 1

            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if count[i] <= 0:
                            return False
                        count[i] -= 1
                start += 1
        return True