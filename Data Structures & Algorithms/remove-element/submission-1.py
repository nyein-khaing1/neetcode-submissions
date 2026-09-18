class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # k = position where we put the next number we want to keep
        # Example:
        # nums = [3, 2, 2, 3]
        # val = 3

        for i in range(len(nums)):
            # i checks every number one by one
            # i = 0, 1, 2, 3

            if nums[i] != val:
                # Keep the number only if it is NOT equal to val
                #
                # Example:
                # i = 0 -> nums[0] = 3 -> 3 != 3 is False -> skip
                # i = 1 -> nums[1] = 2 -> 2 != 3 is True -> keep it

                nums[k] = nums[i]
                # Copy the number at i into position k
                #
                # Example:
                # i = 1, k = 0
                # nums[k] = nums[i]
                # nums[0] = nums[1]
                # nums[0] becomes 2
                #
                # beginning of nums is now:
                # [2, ...]

                k += 1
                # Move k to the next available position
                #
                # Example:
                # k was 0
                # now k = 1
                #
                # Next kept number will go into index 1

        return k
        # k tells us how many numbers we kept
        #
        # Example:
        # nums = [3, 2, 2, 3]
        # after removing 3s, the kept numbers are [2, 2]
        # so k = 2