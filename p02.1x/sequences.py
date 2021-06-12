"""
Problem:

    
The function in_sequence takes in 3 inputs: a, b and t.

    
If t is present in the sequence an + b, it prints which term it is in
    
the sequence, otherwise it prints out "Not present".

    
For example:

    
in_sequence(3, 2, 14) is looking at the sequence 3n + 2.
    
The terms in this sequence are: 5, 8, 11, 14, 17, 20, ...
    
14 is the 4th term in this sequence so the function would print out 4.

    
in_sequence(7, -2, 25) is looking at the sequence 7n - 2.
    
The terms in this sequence are 5, 12, 19, 26, 33, ....
    
25 is not present in this sequence so the function would print "Not present"

Tests:

    
>>> in_sequence(3, 2, 14)
4
    
>>> in_sequence(5, -3, 37)
8
    
>>> in_sequence(-2, 20, 28)
Not present
    
>>> in_sequence(6, 3, 23)
Not present
    
>>> in_sequence(-3, 100, 1)    
33
"""
import doctest, math
def run_tests():
    doctest.testmod(verbose=True)

def in_sequence(a, b, t):
    # Achieved by rearrangement of an + b = t
    term = (t - b) / a 
    if term.is_integer() and term > 0:
        print(int(term))
    else:
        print("Not present") 

if __name__ == "__main__":
    run_tests()