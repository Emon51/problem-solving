"""
GeeksforGeeks has introduced a special offer where you can enroll in any course, and if you manage to complete 90% of the course within 90 days, you will receive a refund of 90%.

Geek was fascinated by this offer. This offer was valid for only n days, and each day a new course was available for purchase. Geek decided that if he bought a course on some day, he will complete that course on the same day itself and redeem floor[90% of cost of the course] amount back. Find the maximum number of courses that Geek can complete in those n days if he had total amount initially.

Note: On any day, Geek can only buy the new course that was made available for purchase that day.

Example 1:

Input:
n = 2
total = 10
cost = [10, 9]
Output: 2
Explanation: 
Geek can buy the first course for 10 amount, 
complete it on the same date and redeem 9 back. 
Next, he can buy and complete the 2nd course too.
Example 2:

Input:
n = 11
total = 10
cost = [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Output: 10
Explanation: 
Geek can buy and complete all the courses that cost 1.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function max_courses() that takes N the number of days, the total amount, and the cost array as input argument and return the maximum amount of courses that could be purchased.

Expected Time Complexity: O(n*total)
Expected Auxiliary Space: O(n*total)

Constraints:
1 <= n <= 1000
0 <= total <= 1000
1 <= cost[i] <= 1000
"""
#TLE
class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        
        def dfs(i, cost, amnt):
            if i >= len(cost):
                return 0
            
            pick =  0
            if cost[i] <= amnt:
                pick = 1 + dfs(i + 1, cost, amnt - cost[i] + int(cost[i] * 0.9))
            notPick = dfs(i + 1, cost, amnt)
            return max(pick, notPick)
            
        return dfs(0, cost, total)





#Accepted
class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        
        def dfs(i, cost, amnt, dp = {}):
            if i >= len(cost):
                return 0
            if (i, amnt) in dp:
                return dp[(i, amnt)]
            pick =  0
            if cost[i] <= amnt:
                pick = 1 + dfs(i + 1, cost, amnt - cost[i] + int(cost[i] * 0.9))
            notPick = dfs(i + 1, cost, amnt)
            val = max(pick, notPick)
            dp[(i, amnt)] = val 
            return val
            
        return dfs(0, cost, total)
