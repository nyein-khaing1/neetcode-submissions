class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M, R):

            # Split the current part of the array into 2 halves
            # Example:
            # arr = [5, 2, 3, 1]
            # L = 0, M = 1, R = 3
            #
            # left  = arr[0:2] = [5, 2]
            # right = arr[2:4] = [3, 1]

            left = arr[L:M + 1]
            right = arr[M + 1:R + 1]

            # i = position in the original array
            # j = position in left
            # k = position in right
            #
            # Example:
            # i = L = 0
            # j = 0
            # k = 0
            i, j, k = L, 0, 0

            # Keep comparing while both left and right
            # still have numbers
            while j < len(left) and k < len(right):

                # Compare the current number from left
                # with the current number from right
                #
                # Example:
                # left = [2, 5]
                # right = [1, 3]
                #
                # left[j] = 2
                # right[k] = 1

                if left[j] <= right[k]:

                    # If the left number is smaller,
                    # put it into the original array
                    arr[i] = left[j]

                    # Move to the next number in left
                    j += 1

                else:

                    # If the right number is smaller,
                    # put it into the original array
                    arr[i] = right[k]

                    # Move to the next number in right
                    k += 1

                # Move to the next position
                # in the original array
                i += 1

            # If there are any numbers left in left,
            # copy them into the original array
            #
            # Example:
            # left = [5]
            # right is already finished
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            # If there are any numbers left in right,
            # copy them into the original array
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):

            # If l and r are the same,
            # there is only 1 number
            #
            # Example:
            # [5]
            #
            # One number is already sorted,
            # so stop here
            if l >= r:
                return arr

            # Find the middle index
            #
            # Example:
            # l = 0, r = 3
            # m = (0 + 3) // 2
            # m = 1
            m = (l + r) // 2

            # Sort the left half
            #
            # Example:
            # [5, 2, 3, 1]
            # sort [5, 2]
            mergeSort(arr, l, m)

            # Sort the right half
            #
            # Example:
            # sort [3, 1]
            mergeSort(arr, m + 1, r)

            # After both halves are sorted,
            # merge them together
            #
            # Example:
            # [2, 5] and [1, 3]
            # becomes
            # [1, 2, 3, 5]
            merge(arr, l, m, r)

            return arr


        # Start merge sort on the whole array
        #
        # Example:
        # nums = [5, 2, 3, 1]
        #
        # start = 0
        # end = 3
        return mergeSort(nums, 0, len(nums) - 1)