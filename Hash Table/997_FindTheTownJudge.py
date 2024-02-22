'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.
If the town judge exists, then:
The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. 
If a trust relationship does not exist in trust array, then such a trust relationship does not exist.
Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 
Constraints:
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''

# The function aims to find the "judge" - a person who is trusted by everyone else but trusts nobody themselves.
# Brief Approach:
# If there are no trust relationships and there is only one person (n == 1), that person is considered the judge.
# Otherwise, it iterates through the trust relationships, counting how many people trust each person (d1) and how many people each person trusts (d2).
# Then, it checks if there is a person who is trusted by n - 1 people (d1[key] == n - 1) and doesn't trust anyone (key not in d2). If found, that person is returned as the judge.
# If no judge is found, it returns -1.


# Its like voting, The person which get all vote ( n-1 ) and same person haven't vote anyone. We need to find this person , if exists then idx of that person otherwise -1.
# We can maintain two arrays , count of vote received and count of vote given for each person.
# Then search for person who have received n-1 vote and not gave single vote.

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if n==1:
                return 1
            else:
                return -1
        d1={}
        d2={}        
        for t in trust:
            if t[1] in d1:
                d1[t[1]]+=1
            else:
                d1[t[1]]=1
            if t[0] in d2:
                d2[t[0]]+=1
            else:
                d2[t[0]]=1
        for key in d1:
            if d1[key]==n-1:
                if key not in d2:
                    return key
        return -1

# Shortened code
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1 if n == 1 else -1
        d1 = {}
        d2 = {}
        for t in trust:
            d1[t[1]] = d1.get(t[1], 0) + 1
            d2[t[0]] = d2.get(t[0], 0) + 1
        for key in d1:
            if d1[key] == n - 1 and key not in d2:
                return key
        return -1
