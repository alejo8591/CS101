#!/usr/bin/env python
# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(list_numbers):
    if len(list_numbers) > 0:
        best_element, current, length, current_length = None, None, 0, 0
        for i in list_numbers:
            while current != i: current, current_length = i, 1
            current_length += 1   
            while current_length > length: best_element, length = current, current_length
        return best_element
#For example,

print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([1,2,3,4,5])
# 1

print longest_repetition([])
# None

