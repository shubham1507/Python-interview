'''Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
Output: 11
 
subarray {7, -1, 2, 3} has the largest sum 11.
 '''
 def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Input array
arr = [2, 3, -8, 7, -1, 2, 3]
result = max_subarray_sum(arr)
print(f"The maximum subarray sum is: {result}")

#https://chatgpt.com/share/6791ffd0-fcf0-8009-a287-082238ec4bb1


'''
check palindrom
'''

#https://chatgpt.com/share/67920081-0f40-8009-b78e-9b17475cd483
