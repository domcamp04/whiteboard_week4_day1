# #Given two strings, return true if they are anagrams of eachother, and false otherwise.
# s1 = "anagram"
# t1 = "nagaram"
# # Output:
# # True
# s2 = "rat"
# t2 = "car"
# #Output:
# # False

def anagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    
    
    list1 = sorted(list1)
    list2 = sorted(list2)
    if list

def anagram(s, t):
    l1 = list(s)
    l2 = list(t)
    
    l1.sort()
    l2.sort()
    if l1 == l2:
        print("The words are anagrams.")
    else:
        print("The words are not anagrams.")

anagram('anagram', 'nagaram')
anagram('car','rat')