'''
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
-231 <= val <= 231 - 1
At most 2 * 105 calls will be made to insert, remove, and getRandom.
There will be at least one element in the data structure when getRandom is called.
'''

'''
Approach:

Initialization:
The class RandomizedSet is initialized with an empty list (mylist) to store unique elements.

Insertion (insert method):
Checks if the given value (val) is already present in the list (mylist).
If not present, appends the value to the list and returns True to indicate successful insertion.
If the value is already present, returns False.

Removal (remove method):
Checks if the given value (val) is present in the list (mylist).
If present, removes the value from the list and returns True to indicate successful removal.
If the value is not present, returns False.

Random Element Retrieval (getRandom method):
Generates a random index (r) between 0 and the length of the list (mylist) minus 1.
Returns the element at the randomly generated index.
'''

class RandomizedSet(object):

    def __init__(self):
        self.mylist=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mylist:
            return False
        else:
            self.mylist.append(val)
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.mylist:
            self.mylist.remove(val)
            return True
        else:
            return False
            
    def getRandom(self):
        """
        :rtype: int
        """
        r=random.randint(0,len(self.mylist)-1)
        return self.mylist[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
