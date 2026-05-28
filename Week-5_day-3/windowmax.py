from collections import deque

def sliding_window_max(nums, k):
    dq = deque()  
    result = []

    for i in range(len(nums)):
        
# Remove elements out of window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

# Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
#Add current index
        dq.append(i)
# Start adding results after first window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(sliding_window_max(arr, k))