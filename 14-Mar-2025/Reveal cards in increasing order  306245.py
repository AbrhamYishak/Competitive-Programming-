# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque()
        for i in range(len(deck)-1,-1,-1):
            if not q:
                q.append(deck[i])
            else:
                q.appendleft(deck[i])
                if i!= 0:
                    a = q.pop()
                    q.appendleft(a)
        return list(q)
        