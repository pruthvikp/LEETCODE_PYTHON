'''
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
 
Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106
'''

# Approach:
# The method first sorts the intervals based on their start times. 
# Then, it iterates through the sorted intervals and checks if there is any overlap between consecutive intervals. 
# If an overlap is found (i.e., if the end time of the current interval is greater than the start time of the next interval), it returns False indicating that it's not possible to attend all meetings without conflicts. 
# If no overlaps are found, it returns True, indicating that all meetings can be attended without conflicts.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
