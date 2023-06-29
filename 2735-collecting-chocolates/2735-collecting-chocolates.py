class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        A = nums[:]
        # rotate min(A) to A[0]
        mi = A.index(min(A))
        A = A[mi:] + A[:mi]
        n = len(A)

        # find next smaller elements on left and right
        left = [0] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] > A[i]:
                right[stack.pop()] = i
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        # delta of delta of results
        res = [0] * (n + 1)
        res[0] = sum(A)
        res[1] = x

        # trapezoid curve for A[i] contribution
        for i in range(1, n):  # trapezoid curve for A[i] contribution
            res[min(i - left[i], right[i] - i)] -= A[i]
            res[max(i - left[i], right[i] - i)] -= A[i]
            res[right[i] - left[i]] += A[i]

        # calculate prefix sum of res for twice
        return min(accumulate(accumulate(res)))