# Variables
# If-else Statements
# Loops
# Math
# ----------Arrays----------

# 1) Reverse an array of intergers

# arr = [1,2,3,4,5]
# arr.sort(reverse=True)

# print(arr)

# 2) Mix and Max in array

# arr = [1,23,4,5,6,78]
# ma = max(arr)
# mi = min(arr)

# print("Max: ", ma)
# print("Min: ", mi)

# 3) Intersection of two unsorted arrays

# arr1 = [1,3,5,2]
# arr2 = [3,1,7,9]


# def intersection(arr1, arr2):
#     a = set(arr1)
#     b = set(arr2)

#     result = a & b
#     print(result)

# intersection(arr1, arr2)

# 4) Union of two arrays
# arr1 = [1,2,5,6]
# arr2 = [3,4]

# def union(arr1, arr2):

#     a = set(arr1)
#     b = set(arr2)

    
#     result = a | b

#     print(result)

# union(arr1, arr2)

# 5) Remove duplicacy from array

# arr = [1,1,2,3,4,5,6,7,7]

# def dup(arr):
#     a = set(arr)

#     print(a)

# dup(arr)

# 6) Find the Second largest number in an array

# arr = [1,2,5,4]
# a = max(arr)-1

# print(a)


# 5) Left rotate an array by 1 place

# arr = [1, 2, 3, 4, 5]

# def rotation(arr):
#     if not arr:
#         return arr
    
#     mod_arr = arr[1:] + arr[:1]
#     

# rotation(arr)


# 6) Left rotate an array by D places

# def rotation(arr, d):
#     if not arr:
#         return arr
    
#     n = len(arr)
#     d = d % n # for effective rotation

#     modified_array = arr[d:] + arr[:d]

#     print(modified_array)

# arr = [1, 2, 3, 4, 5]
# rotation(arr, 2)


# 7) Right rotate an array by D places

# def right_rotation(arr, d):
#     if not arr:
#         return arr
    
#     n = len(arr)
#     d = n - (d % n)

#     modified_array = arr[:d] + arr[d:]

#     print(modified_array)

# arr = [1, 2, 3, 4, 5]
# right_rotation(arr, 1)


# 8) Moving zeroes to end

# def zeroes(arr):
#     non_zero = []
#     count_zero = 0

#     for i in arr:
#         if i != 0:
#             non_zero.append(i)

#         else:
#             count_zero += 1

#     result = non_zero + [0] * count_zero
#     return result
# arr = [1,0,2,3,5,6]  
# zeroes(arr)

# 9) Linear search basic question

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if the target is found
#     return -1  # Return -1 if the target is not found

# arr = [4, 2, 7, 1, 9, 5]
# target = 7
# result = linear_search(arr, target)
# if result != -1:
#     print(f"Element {target} found at index {result}")
# else:
#     print(f"Element {target} not found in the array")



  
    






        










     





    

    





















# Strings
# Queues
# HashSets / Sets
# HashMaps / Dictionary
# Tuples
# Heaps
# Functions
# Classes
