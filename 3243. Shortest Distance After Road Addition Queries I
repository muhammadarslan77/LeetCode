class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        dic = {end: [end-1] for end in range(1, n)} # add the original 1-step arrows
        res = []
        for j in range(len(queries)):
            dp = [0 if i == 0 else n for i in range(n)]
            dic[queries[j][1]].append(queries[j][0])
            for i in range(1, n):
                for start in dic[i]:
                    dp[i] = min(dp[i], dp[start]+1)
            res.append(dp[-1])
        return res
