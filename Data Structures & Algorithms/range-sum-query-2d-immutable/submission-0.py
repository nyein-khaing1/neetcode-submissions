class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        # Get number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Create prefix sum matrix with an extra row and column of 0s
        self.sumMat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):

            # Running sum for the current row
            prefix = 0

            for c in range(COLS):

                # Add current value to row prefix
                prefix += matrix[r][c]

                # Get everything above this cell
                above = self.sumMat[r][c + 1]

                # Current prefix sum =
                # row prefix + everything above
                self.sumMat[r + 1][c + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        # Convert original matrix indexes to prefix matrix indexes
        r1, c1 = row1 + 1, col1 + 1
        r2, c2 = row2 + 1, col2 + 1

        # Total area from (0,0) to bottom-right
        bottomRight = self.sumMat[r2][c2]

        # Remove area above the rectangle
        above = self.sumMat[r1 - 1][c2]

        # Remove area to the left of the rectangle
        left = self.sumMat[r2][c1 - 1]

        # We removed the top-left area twice,
        # so we need to add it back once
        topLeft = self.sumMat[r1 - 1][c1 - 1]

        return bottomRight - above - left + topLeft