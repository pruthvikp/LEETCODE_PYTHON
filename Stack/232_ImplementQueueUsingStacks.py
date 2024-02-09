'''
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:
void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.

Notes:
You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
Example 1:
Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]
Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
 
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.
 
Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
'''

# To enqueue, we use the two stacks stack1 and stack2. Initially, all elements are stored in stack1 and stack2 is empty. 
# In order to add an element to the back of the queue, first transfer all elements from stack1 to stack2 using a loop that pops each element from stack1 and pushes it onto stack2.
# Once all elements have been transferred to stack2, push the new element onto stack1.
# Finally, transfer all elements from stack2 back to stack1 in the same way as before, so that the queue maintains its ordering.

class MyQueue(object):

    def __init__(self):
        self.queue=[]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        que=[]
        while not self.empty():
            que.append(self.queue.pop())
        self.queue.append(x)
        while que:
            self.queue.append(que.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()       

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
