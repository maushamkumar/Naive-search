# Binary_search Algorithm
# ----------------------

def Binary_search(l,target):
    """Parameters:
    - lst (list): The list in which the search is conducted.
    - target: The element to be found in the list.
    - midpoint: midpoint of the list """
    
    midpoint = len(list)//2
    
    if l[midpoint] == target:
         return midpoint
     
    elif target < l[midpoint]:
        return Binary_search(l,target,midpoint -1)
    else:
        return Binary_search(l,target,midpoint + 1)
    
    
lst = [12,3,45,3,5,35,5]
print(Binary_search(lst,3))

