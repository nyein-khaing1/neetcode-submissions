class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # If there is only 1 number, it is already sorted
        if len(nums) <= 1:
            return nums

        # Find the middle
        mid = len(nums) // 2

        # Split the array into left and right
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        # This will store the sorted result
        result = []

        i = 0  # pointer for left
        j = 0  # pointer for right

        # Compare numbers from left and right
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add any numbers left over
        result.extend(left[i:])
        result.extend(right[j:])

        return result