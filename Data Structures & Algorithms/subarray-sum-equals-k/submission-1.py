class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # How many valid subarrays we found
        res = 0

        # Running total from the start up to current position
        curSum = 0

        # Stores:
        # prefix sum -> how many times we have seen it
        #
        # 0 : 1 means "before reading any numbers,
        # we have seen a sum of 0 once"
        prefixSums = {0: 1}

        for n in nums:

            # Add current number to running sum
            curSum += n

            # We want to know:
            # was there an earlier prefix sum such that
            # curSum - earlierSum = k ?
            #
            # Rearranged:
            # earlierSum = curSum - k
            diff = curSum - k

            # If we have seen 'diff' before,
            # then each time we saw it gives us
            # one subarray ending here with sum k
            res += prefixSums.get(diff, 0)

            # Record that we have now seen curSum
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)

        return res