class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        ind = sorted(range(n), key=positions.__getitem__)
        
        stack = []
        for i in ind:
            if directions[i] == "R":
                stack.append(i)
                continue
            while len(stack) > 0 and healths[i] > 0:
                if healths[stack[-1]] > healths[i]:
                    healths[i] = 0
                    healths[stack[-1]] -= 1
                elif healths[stack[-1]] < healths[i]:
                    healths[stack.pop()] = 0
                    healths[i] -= 1
                else:
                    healths[stack.pop()] = 0
                    healths[i] = 0
        return [v for v in healths if v > 0]
                    
                