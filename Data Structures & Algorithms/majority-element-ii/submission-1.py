from collections import defaultdict
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # This dictionary stores possible majority candidates
        # and their current "vote" count.
        count = defaultdict(int)

        # Go through every number in nums
        for n in nums:

            # Add 1 vote for this number
            count[n] += 1

            # For the n/3 problem, there can be at most
            # 2 majority elements.
            # So if we only have 1 or 2 candidates,
            # we can keep them for now.
            if len(count) <= 2:
                continue

            # If we have 3 different candidates,
            # we need to cancel one vote from each.
            new_count = defaultdict(int)

            for num, c in count.items():

                # If the count is greater than 1,
                # subtract one and keep the candidate.
                if c > 1:
                    new_count[num] = c - 1

                # If c == 1, subtracting one makes it 0,
                # so we don't add it to new_count.

            # Replace count with the reduced candidates
            count = new_count

        # count now contains POSSIBLE answers,
        # but we still need to check their real frequency.
        res = []

        for n in count:

            # Count how many times n really appears in nums.
            # It must appear more than n/3 times.
            if nums.count(n) > len(nums) // 3:
                res.append(n)

        return res