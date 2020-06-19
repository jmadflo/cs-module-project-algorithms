'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # max_vals = []
    # for num in range(k, len(nums) + 1):
    #     window = nums[num - k: num]
    #     max_vals.append(max(window))
    # return max_vals

    # return [max(nums[num - k: num]) for num in range(k, len(nums) + 1)]

    if k >= len(nums):
        return max(nums)

    # add the initialize the window_max value and the all_max list
    window_max = max(nums[:k])
    all_max = [window_max]

    for i in range(len(nums) - k):
        # If the element that the window is leaving behind is the window_max, then recalculate the mask with the new window.
        if nums[i] == window_max:
            window_max = max(nums[i+1:i+k+1]) 
        # If the new element is greater than the current window_max, then make the new element the max
        if nums[i+k] > window_max:
            window_max = nums[i+k]
        # Add the max for this window to the all_max list
        all_max.append(window_max)
    return all_max

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
