'''
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 
Constraints:
10 <= low <= high <= 10^9
'''

# The code iterates through all possible substrings of the string "123456789" and checks if the integer representation of each substring falls within the given range. 
# If it does, the integer is added to the result list.
# Finally, it returns the sorted result list.

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res=[]
        string="123456789"
        for i in range(len(string)):        
            for j in range(i+1,len(string)):
                if low<=int(string[i:j+1])<=high:
                    res.append(int(string[i:j+1]))
        return sorted(res)
              
