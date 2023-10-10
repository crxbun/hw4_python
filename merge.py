#Quicksort algorithm
"""
Pivot is always the last element of the list. i starts
before the start element of the list, and j starts at the
starting element of the list.

if element at j is less than the pivot element, we 
increment i and swap the element at j with the element at
i.

if element at j is not less than the pivot element, we
do not increment i. 

once j reaches pivot, we increment i one more time and swap
element at i with pivot (element at j). this is the correct
spot for pivot

all elements left of pivot are lower than pivot, all elements
right of pivot are higher than pivot

from there, we split into subproblems and quicksort each
subproblem (divide and conquer)
"""
def partition(list: list, low: int, high: int):
    pivot = list[high] # pivot begins at end of list
    i = low - 1 # index i starts at left from the first element

    for j in range(low, high):
        if list[j] <= pivot: # if element is less than pivot, we want it to the lefthand side
            i = i + 1 # iterate i index for every iteration
            (list[i], list[j]) = (list[j], list[i]) # swap when pivot is less than pivot
    
    i = i + 1 # once all elements are in proper positioning to swap in pivot, increment i to move to correct position for pivot element
    (list[i], list[high]) = (list[high], list[i]) # swap pivot element with element at i; now all elements less than pivot are to
                                                  # the left and more than pivot are to the right

    return i # location of the pivot
    
def sort(list:list, start:int, end:int):
    if start >= end: # no further partitioning is needed for lists with zero or one element, assume sorted
        return
    
    pivot = partition(list, start, end)
    sort(list, start, pivot - 1)
    sort(list, pivot + 1, end)
    

def merge_list(list1, list2: list) -> list:
    solution = []
    for x in list1:
        solution.append(x)

    for x in list2:
        solution.append(x)
    
    sort(solution, 0, len(solution) - 1)
    return solution