def my_steps(n: int) -> int:
    """
    Dynamic programming approach for calculating how many different ways we can
    go up a set of n stairs given we can take 1 or 2 steps each time.
    """
    if (n < 1 or n > 25):
        raise ValueError
    
    one_step, two_steps = 1, 1

    for i in range(n - 1):
        tmp = one_step
        one_step = one_step + two_steps
        two_steps = tmp
    
    return one_step

# Dynamic Approach
"""
Tree
                                      0
                         1                           2
                  2              3           3               4
            3          4       4  [5]     4  [5]         [5]  6
          4   [5]    [5] 6  [5] 6       [5] 6 
       [5] 6  
                 
my_steps(5)

n = 5

# represents ways to go from 4 to 5 and ways to go from 5 to 5
one, two = 1, 1

for i in range(n - 1) # i in range 0 to 3 (inclusive)

# represents ways to go from 3 to 5 ...
first iteration (when i = 0)
    tmp = 1
    one = 1 + 1 # ways to go from 3 to 5 = ways to go from 4 to 5 + ways to go from 5 to 5
    two = tmp # shift two step var to prev (due to bottom up); represents 2 steps from 2 = ways to go from 4 to 5

# represents ways to go from 2 to 5
second iteration (when i = 1)
    tmp = 2 # store value of current one step to shift two step later
    one = 2 + 1 # ways to go from 2 to 5 = ways to go from 3 to 5 (1 step) + ways to go from 4 to 5 (two steps)
    two = tmp # shift two step var to prev (due to bottom up); represents 2 steps from 1 = ways to go from 3 to 5

# ways to go from 1 to 5
third iteration (when i = 2)
    tmp = 3 # store value of current one step to shift two step later
    one = 5 # 3 + 2; ways to go from 1 to 5 = ways to go from 2 to 5 (1 step) + ways to go from 3 to 5 (two steps)
    two = tmp # shift two step var to prev (due to bottom up); represents 2 steps from 0 = ways to go from 2 to 5

# ways to go from 0 to 5
fourth iteration (when i = 3)
    tmp = 5 # store value of current one step to shift two step later
    one = 5 + 3 # ways to go from 0 to 5 (solution) 
    two = tmp # solution is already stored in one

return one_step -> ways to go from 0 steps to the 5th step
"""
