
'''
Given an array arr[] containing N integers. In one step, any element of the array can either be increased or decreased by one. Find minimum steps required such that the product of the array elements becomes 1.

 

Example 1:

Input:
N = 3
arr[] = {-2, 4, 0}
Output:
5
Explanation:
We can change -2 to -1, 0 to -1 and 4 to 1.
So, a total of 5 steps are required
to update the elements such that
the product of the final array is 1. 
Example 2:
Input:
N = 3
arr[] = {-1, 1, -1} 
Output :
0
Explanation:
Product of the array is already 1.
So, we don't need to change anything.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function makeProductOne() which takes an integer N and an array arr of size N as input and returns the minimum steps required.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 105
-103 ≤ arr[i] ≤ 103

Company Tags
Amazon, Microsoft
'''

#User function Template for python3

class Solution:
    def makeProductOne(self, arr, N):
        
        neg, zero = 0, 0 
        res = 0 
        for num in arr:
            if num == 0:
                zero += 1
            elif num < 0:
                neg += 1
                if num != -1:
                    res += abs(num) - 1
            else:
                res += (num - 1)
                
        if neg % 2 == 1 and 0 < zero:
            return  res + zero 
        if neg % 2 == 1:
            return res + 2
        return res + zero
        


















