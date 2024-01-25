'''
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Example 1:
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255

Tip:
You have a grid filled with numbers, which we will call an "image". You are asked to create a new image where the value of each cell is the average of itself and its neighbors. 
However, if a cell doesn't have a neighbor in any direction (because it's on the edge), just ignore that non-existing neighbor when computing the average.
For instance, the cell at the top left corner has only three neighbors (right, down-right, down), while a cell in the middle of the image has eight neighbors (up, down, left, right, and all the four diagonals).
The goal is to create a new image with these averaged values. Round down the average if it's not an integer.
'''

# Brief Approach:
# Initialize an empty matrix res of the same size as the input img to store the smoothed image.
# Iterate through each cell in the input matrix img.
# For each cell, initialize variables total and count to calculate the sum and count of valid surrounding cells.
# Use nested loops to iterate through the 3x3 neighborhood around the current cell.
# For each neighboring cell, check if it is within the image boundaries (0 <= x < m and 0 <= y < n).
# If the neighboring cell is valid, update total by adding its value and increment the count.
# Calculate the average as total // count and store it in the corresponding cell of the result matrix res.
# Return the smoothed image res.

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n=len(img),len(img[0])
        res=[]
        for _ in range(m):
            res.append([0]*n)
        
        for i in range(m):
            for j in range(n):
                total,count=0,0
                for k in range(-1,2):
                    for l in range(-1,2):
                        x,y=i+k,j+l
                        if 0<=x<m and 0<=y<n:
                            total+=img[x][y]
                            count+=1
                res[i][j]=total//count
                
        return res
