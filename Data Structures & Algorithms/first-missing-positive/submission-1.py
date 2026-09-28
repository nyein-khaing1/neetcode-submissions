class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:

        # Step 1:
        # Replace all negative numbers with 0.
        # We only care about positive numbers from 1 to len(A).
        for i in range(len(A)):
            if A[i] < 0:
                A[i] = 0

        # Step 2:
        # Use the array itself to mark which numbers exist.
        for i in range(len(A)):

            # Get the actual value because some values may already be negative.
            val = abs(A[i])

            # Only care about values between 1 and len(A).
            if 1 <= val <= len(A):

                # val = 1 means use index 0
                # val = 2 means use index 1
                # val = 3 means use index 2
                # So we use val - 1 as the index.

                if A[val - 1] > 0:

                    # Make this position negative to show that 'val' exists.
                    A[val - 1] *= -1

                elif A[val - 1] == 0:

                    # We cannot make 0 negative because -0 is still 0.
                    # So use a negative number instead to mark it.
                    A[val - 1] = -(len(A) + 1)

        # Step 3:
        # Look for the first position that is NOT negative.
        # That means that number was never found in the array.
        for i in range(1, len(A) + 1):

            if A[i - 1] >= 0:
                return i

        # If every number from 1 to len(A) exists,
        # then the missing positive number must be len(A) + 1.
        return len(A) + 1