'''

https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''

'''
TC = O(len(s))
SC = O(n). Using hashmap to store the pairs
'''

    
def is_anagram(s: str, t: str) -> bool:
        
    
        if len(s) != len(t):
            return False
         
        dic = {}
        for item in s:
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1
        
        for item in t:
            if item not in dic:
                return False
            else:
                dic[item] -= 1
                
                if dic[item] == -1:
                    return False
        return True
        
        

print(is_anagram("fairyll b taleso","rail safety boll"))