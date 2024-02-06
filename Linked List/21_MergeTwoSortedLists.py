'''
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
'''

# Approach:
# Initialize a dummy node and a temporary node temp to construct the merged list.
# Iterate through both lists simultaneously using a while loop.
# Compare the values of the current nodes from list1 and list2.
# Connect the smaller node to temp.next, update temp to the smaller node, and move to the next node in the respective list.
# Continue this process until reaching the end of either list.
# If one of the lists still has remaining nodes after the loop, connect the remaining nodes directly to temp.next.
# Return the next node of the dummy node, which is the head of the merged list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=temp=ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                temp.next=list1
                temp=list1
                list1=list1.next                
            else:
                temp.next=list2
                temp=list2
                list2=list2.next
        if list1 or list2:
            temp.next=list1 if list1 else list2
        return dummy.next
      
