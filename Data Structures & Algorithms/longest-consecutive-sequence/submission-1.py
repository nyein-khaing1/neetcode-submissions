class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Convert the list into a set
        # This lets us check if a number exists very quickly: O(1)
        numSet = set(nums)

        # Stores the longest consecutive sequence found
        longest = 0

        # Go through every number
        for n in nums:

            # Check if n is the START of a sequence
            #
            # Example:
            # nums = [100, 4, 200, 1, 3, 2]
            #
            # If n = 1:
            # 0 is NOT in the set
            # so 1 must be the start of a sequence
            #
            # If n = 2:
            # 1 IS in the set
            # so 2 is not the start, we skip it
            if (n - 1) not in numSet:

                # Length of the current sequence
                length = 0

                # Keep checking the next consecutive numbers
                #
                # If n = 1:
                # 1 + 0 = 1 -> exists
                # 1 + 1 = 2 -> exists
                # 1 + 2 = 3 -> exists
                # 1 + 3 = 4 -> exists
                # 1 + 4 = 5 -> does not exist
                while (n + length) in numSet:
                    length += 1

                # Compare this sequence length with the longest
                # sequence we have found so far
                longest = max(length, longest)

        # Return the longest consecutive sequence length
        return longest