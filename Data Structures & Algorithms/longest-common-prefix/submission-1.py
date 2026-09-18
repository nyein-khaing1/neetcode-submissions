class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""  
        # Example: strs = ["flower", "flow", "flight"]
        # res starts as ""

        for i in range(len(strs[0])):
            # strs[0] = "flower"
            # i goes through the indexes: 0, 1, 2, 3, 4, 5

            for s in strs:
                # s goes through each word:
                # s = "flower"
                # s = "flow"
                # s = "flight"

                # i == len(s)
                # means we reached the end of the current word

                # s[i]
                # means the letter at index i in the current word

                # strs[0][i]
                # means the letter at index i in the first word

                # Example when i = 2 and s = "flight":
                # s[i] = "flight"[2] = "i"
                # strs[0][i] = "flower"[2] = "o"
                # "i" != "o", so we stop
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # If every word has the same letter at index i,
            # add that letter to res

            # Example:
            # i = 0 -> all words have "f" -> res = "f"
            # i = 1 -> all words have "l" -> res = "fl"
            res += strs[0][i]

        return res