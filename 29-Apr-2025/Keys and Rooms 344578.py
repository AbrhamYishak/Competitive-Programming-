# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        q = deque()
        for i in rooms[0]:
            q.append(i)
        while q:
            a = q.popleft()
            seen.add(a)
            for j in rooms[a]:
                if j not in seen:
                    q.append(j)
        return len(seen) == len(rooms)