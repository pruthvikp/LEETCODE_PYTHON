'''
You are given two linked lists: list1 and list2 of sizes n and m respectively.
Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

Build the result list and return its head.

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

Example 2:
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 
Constraints:
3 <= list1.length <= 104
1 <= a <= b < list1.length - 1
1 <= list2.length <= 104
'''

# Approach:
# Traverse list1 until reaching the node before position a. This is done by moving ptr forward a-1 times.
# Save the current node (node before position a) as save.
# Move ptr forward b-a+1 times to reach the node after position b.
# Connect the next pointer of save to the head of list2, effectively attaching list2 to list1 at position a.
# Traverse list2 until reaching its last node (ptr2).
# Connect the last node of list2 to the node after position b in list1.
# Set the next pointer of the last node of list2 to None to terminate the merged list.
# Return list1 which now contains list2 merged between positions a and b.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr=list1
        for _ in range(a-1):
            ptr=ptr.next
        save=ptr
        for _ in range(b-a+1):
            ptr=ptr.next
        save.next=list2
        ptr2=list2
        while ptr2.next:
            ptr2=ptr2.next
        ptr2.next=ptr.next
        ptr.next=None
        return list1
