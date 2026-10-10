# 1. Repeat the problem in your own words.
# given an input arrary and some target in this case 7
# so I need to find two values in this input arrary that add up to the target and return their indices

#2. Clarify anything important.
#Can I assume there is always exactly one solution?” or “Can the array contain duplicate values?”

# 3.Mention the simple approach first.
#start at first number, every combination we make that includes first number, scan through the remainding arrary and sum up to the target , repeat the process
#brute force ( go through entire array of length(n) and worst case (n*n)for each number, overall worse case time complexity  O(n)2 )

#4.Can we do better?
#harsh map of every value in our input array so we can instantly check if the value (4-1) = 3 exists if the target is 4
#in Harsh map, going to mapping each value to the index of each value
#Mapping the value to the index
#4-2 exist in the hashmap, cannot use the same value twice
#if the hashmap is empty , add it to the hashmap
#continue the process 
#if it does exist, found our two values sum to the target, return to their indices
#iterate through the array in one pass
#have to iterate once , adding each value to our hash map is a constant time operation  and if a value exists in our hashmap which is also a constant time operation (time complexity O(n))
#extra memory for hashmap (memory complexity O(n), we could potentially add every value to the hashmap )







class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        #every previous element is stored in this map
        #value : index

        for i, n in enumerate(nums):
        #we need the index, as well as the number
            diff = target - n
            #before we add this to the map
            #if the diff is already in hashmap

            if diff in prevMap:
                return[prevMap[diff], i]
                #a pair of the indices 

            prevMap[n] = i
            #dont find the solution, update the hashmap
        return
        