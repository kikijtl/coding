class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # Keep a count list for each interval:
        # [0, 1), [1, 2), [2, 3), ..., [n-1, n),
        # [n, infinity)
        n = len(citations)
        count_ls = [0] * (n + 1)
        for i in range(n):
            if citations[i] <= n:
                # Add count for interval [citations[i], citations[i+1])
                count_ls[citations[i]] += 1
            else:
                # Add count for interval [n, infinity)
                count_ls[n] += 1
        accumulative_count = 0
        for i in range(len(count_ls)-1, -1, -1):
            # Sum up the accumulative_count from the back of the count_ls
            accumulative_count += count_ls[i]
            if accumulative_count >= i:
                return count_ls[i]

if __name__ == '__main__':
    solution = Solution()
    citations = [0, 1]
    print solution.hIndex(citations)
    