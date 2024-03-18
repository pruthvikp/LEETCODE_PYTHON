'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
 
Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 
Constraints:
1 <= points.length <= 105
points[i].length == 2
-231 <= xstart < xend <= 231 - 1
'''

# Brief Approach:
# Sort the intervals based on their end points.
# Initialize a count to 1 and set the variable first to the end point of the first interval.
# Iterate through the sorted intervals:
# If the start point of the current interval is greater than first, it implies a new arrow is needed. Increment the count and update first to the end point of the current interval.
# Return the count as the result, which represents the minimum number of arrows required to burst all the balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points, key=lambda x:x[1])
        count=1
        first=points[0][1]
        i,n=1,len(points)
        while i<n:
            if points[i][0]>first:
                count+=1
                first=points[i][1]
            i+=1
        return count
