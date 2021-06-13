"""
Problem:

    
The function `uniq_insert` takes two arguments, a list, nums, and an integer, n.
    
If nums already contains n, it should do nothing.
    
Otherwise, it should append n to the end of nums.
    
In both cases, print out the new list.


Tests:

    
>>> uniq_insert([1, 2, 3], 4)
[1, 2, 3, 4]
    
>>> uniq_insert([1, 2, 3, 4], 4)
[1, 2, 3, 4]
    
>>> uniq_insert([5, 9, 8], 7)
[5, 9, 8, 7]
    
>>> uniq_insert([3, 6, 5, 2], 5)
[3, 6, 5, 2]
"""
import doctest
def run_tests():
    doctest.testmod(verbose=True)

def uniq_insert(nums, n):
    if n not in nums:
        nums.append(n)

    print(nums)

if __name__ == "__main__":
    run_tests()

