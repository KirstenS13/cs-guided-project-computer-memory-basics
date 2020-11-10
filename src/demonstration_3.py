"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # Your code here
    # UNDERSTAND
    # if the count = value, return the value

    # PLAN
    # Define an output variable
    # output = -1
    # # Sort the list from largest to smallest
    # lst.sort(reverse=True)  # sort --> O(n log n), in place
    # # Make a set
    # set_list = set(lst)     # O(n), O(n) space
    # # Iterate through the set, counting the # of times each value shows up
    # for number in set_list: # O(n)
    #     # Make a count variable
    #     count = lst.count(number)   # O(n), constant space
    #     # Check if the count == the value
    #     if number == count:         # O(1)
    #         # If it does, add it to output variable
    #         output = number         # O(1), constant space
    # # If nothing matches, return -1
    # return output

    # Overall Runtime: 
    #   constant + n log n + n * n --> O(n^2)
    # Space Complexity: O(n)


    # Reduced Time Complexity Version
    output = -1

    lst.sort(reverse=True)

    counts = {}

    for number in lst:              # O(n)
        if number not in counts:
            counts[number] = 0
        counts[number] += 1

    set_list = set(lst)             # O(n)

    for number in set_list:
        count = counts[number]      # O(n)
        if number == count:
            output = number 

    return output

    # Overall Runtime:
    #   O(n log n)

print(find_lucky([2,3,3,4,4,4]))


# Question 7 from Module 3 Project
def increasingSubstrings(s):
    # w/o ord()

    # Overall Runtime: O(n)
    # PLAN
    output = []
    # cur_substring = ""
    cur_substring = ""
    # iterate through s by char
    for c in s:                             # O(n) where n = len(s)
    # compare the current to the prev char
        if cur_substring == "":
            cur_substring = c
            continue
        previous = cur_substring[-1]        # O(1)
    # if it's increasing 
        if is_increasing(previous, c):      # O(1)
    #   then it's part of the same substring, append to cur substring
            cur_substring += c
    # else
        else:
    #   append cur_substring to our output list
            output.append(cur_substring)    # O(1)
    #   start a new cur_substring w/ the cur char
            cur_substring = c               # O(1)
        print(cur_substring)

    if cur_substring:
        output.append(cur_substring)
    # return our output list
    return output

def is_increasing(char1, char2):            # O(1)
    lower = "abcdefghijklmnopqrstuvwxyz"    # O(1)
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    # O(1)

    char1_index = lower.find(char1)         # O(n) where n = 26, so O(26) --> O(1)
    char2_index = lower.find(char2)         # O(26) --> O(1)
    if char1_index == -1:
        char1_index = upper.find(char1)     # O(26) --> O(1)
        char2_index = upper.find(char2)     # O(26) --> O(1)
    # if the index of char2 == index of char1 + 1
    return char2_index == char1_index + 1