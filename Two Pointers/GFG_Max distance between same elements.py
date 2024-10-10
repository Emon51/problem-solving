
'''
Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.
Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.
Expected Time Complexity :  O(n)
Expected Auxilliary Space : O(n)

Constraints:
1 <= arr.size() <= 106
1 <= arr[i] <= 109
'''

class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        
        n = len(arr)
        res = 0
        mapp = {}
        for i in range(n-1, -1, -1):
            if arr[i] not in mapp:
                mapp[arr[i]] = i 
        
        for i in range(n):
            res = max(res, mapp[arr[i]] - i)
        return res 

