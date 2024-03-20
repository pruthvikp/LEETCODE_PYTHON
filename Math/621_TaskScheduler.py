'''
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
​Return the minimum number of intervals required to complete all tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

Constraints:
1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
'''

# Approach:
# https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440

# The trick here is that scheduler doesn’t run the same job again until n units have passed since it ran the same job. So, if we think which job has the most impact of this restriction, we will naturally get the answer that most frequent job will have most impact.

# Case 1:
# Now let’s see what it will take to schedule most frequent job and forget about others. Let’s take a sample: [A, A, A, B, B, C] and cool down time is n = 2. The way to schedule just A would be below, where blank space is idle unit.
# A _ _ A _ _ A. We need 2 idle units and 1 unit for A for each (f-1) A, where f is frequency of A + another 1 unit for last A. So, we found a formula to find number of units needed for most frequent job: (n+1)* (f-1) + 1.

# Case 2:
# Now let’s say there are two elements which are most frequent [A, A, A, B, B, B, C] and n=2. Now we have 3 Bs as well. As you can see that we can just fit the B in existing empty space. And the only extra unit will be needed for last B which is placed at the end next to last A. So, if there are two most frequent element the answer would be: (n+1)*(f-1) + 2.
# Generalizing this if we have X number of most frequent jobs then answer would be (n+1)*(f-1)+X.

# So, these are the number of units needed for most frequent jobs, how about the other jobs that need to be scheduled which are not most frequent.

# Case 3:
# Since, we have some empty space in in each block, we can just place the new jobs in those spaces. And since there frequency is less than they will fit in empty space and won’t go beyond last space.
# Take an example: [A, A, A, B, B, C] can be scheduled as below (Bold ones are the job that is put on empty spaces) A B C A B__ A.
# In above example we are able to schedule other job in the same empty space and didn’t need a new unit. What if we have one more C. That can be fit in another empty space.

# But what if we have two other jobs D and E. Yes, this needs a bit of thinking.
# Case 4:
# If after scheduling most frequent ones and then filling the empty space with other jobs, there are jobs left then we can always extend the block with extra space. Let’s see for example [A, A, A, B, B, C, C, D, E]
# After scheduling most frequent one and then filling B and C, scheduling will look like A B C A B C A. To put D and E we will extend it like below.
# A B C _ A B C_ A
# And put D and E on those empty space. A B C D A B C E A
# Which means that either after scheduling we have some empty spaces left OR all empty spaces are filled and some other empty spaces are created and filled. So how many units are needed for later case: Easy. As many units as there are jobs because there are no empty spaces.

# So final answer is: max ( (n+1)*(f-1) + X, TotalJobs)


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks)
        maxi=max(d.values())
        maxi_keys=[key for key,value in d.items() if value==maxi]
        f,X=maxi,len(maxi_keys)
        return max((n+1)*(f-1)+X,len(tasks))
