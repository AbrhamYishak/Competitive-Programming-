# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        min_force = 0
        max_force = max(position)+1
        n = len(position)
        position.sort()
        check = set(position)
        def validate(f):
            start = min(position)
            for i in range(m-1):
                start+=f
                if start in check:
                    continue
                else:
                    a = bisect_left(position,start)
                    if a == n:
                        return False
                    else:
                        start = position[a]
            return True
        while min_force <= max_force:
            mid = (min_force + max_force)//2
            if validate(mid):
                min_force = mid+1
            else:
                max_force = mid-1
        return max_force

        