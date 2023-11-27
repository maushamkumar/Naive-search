# Naive Search Algorithm
# ----------------------

# The Naive Search algorithm is a straightforward approach to find the index of a target element in a list.
# It iterates through the entire list and checks each element against the target.
# If a match is found, it returns the index of the target; otherwise, it returns -1.

def Naive_search(lst, target):
    """
    Naive Search Algorithm to find the index of the target element in a list.

    Parameters:
    - lst (list): The list to search through.
    - target: The element to find in the list.

    Returns:
    - int: The index of the target element if found, otherwise -1.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

# Example Usage:
# --------------
# Given a list [10, 20, 30, 40, 50], we want to find the index of the target element 20.
# The Naive Search is applied, and the result is printed.

list_to_search = [10, 20, 30, 40, 50]
target_element = 20

result = Naive_search(list_to_search, target_element)
print(f"The index of {target_element} in the list is: {result}")



# Another Example 
# Here is a empty list , you provide your own list and whatever you want to find to search it 
# The Naive Search is applied, and the result is printed.
# -------------------------------------------------------
list = eval(input("Enter your own litst :"))
target = input("Enter your target :")

Alogrithm = Naive_search(list,target)
print(f"The index of {target} in the list is: {Alogrithm}")
