"""
Problem:

    
Given a list of nums, find out whether the first and last items in the list
    
are the same. If they are the same, print "Same"; if not, print "Different".
    
If the list is empty, print "Empty"

Tests:

    
>>> same_ends([1, 2, 3, 2, 1])
Same
    
>>> same_ends([2, 4, 5, 4])
Different
    
>>> same_ends([1])
Same
    
>>> same_ends([])
Empty
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def same_ends(nums):
    if len(nums) == 0:
        print("Empty")
    elif nums[0] == nums[len(nums) - 1]:
        print("Same")
    else:
        print("Different")

if __name__ == "__main__":
    run_tests()