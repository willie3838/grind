
'''
[a,c,d,b,b,c,a] -> [d,d,c,d,c,d,d]

'''
def replace_remove(arr, size):

    # Optimzied solutoin with O(1) space by using multiple passes (forwards and backwards)
    # forward iteration to count as and delete bs
    write_idx, a_count = 0, 0
    for i in range(size):
        if arr[i] != 'b':
            arr[write_idx] = arr[i]
            write_idx += 1
        if arr[i] == 'a':
            a_count += 1
    
    # resets pointer to point to the end of the array we apply the operations to
    curr_idx = write_idx - 1
    # updates pointer to go to the end of the final array we'll be creating
    write_idx += a_count - 1
    # gets the size of the final array we'll create
    final_size = write_idx + 1

    # backwards iteration to replace a with dd
    while curr_idx >= 0:
        if arr[curr_idx] == 'a':
            arr[write_idx - 1 : write_idx + 1] = 'dd'
            write_idx -= 2
        else:
            arr[write_idx] = arr[curr_idx]
            write_idx -= 1
        curr_idx -= 1
    
    return arr[:final_size]
        
    
    # brute force with O(n) space
    # res = ""
    # for char in arr:
    #     if char == "a":
    #         res += "dd"
    #     elif char != "b":
    #         res += char
    
    # return list(res)

print(replace_remove(["a","c","d","b","b","c","a"], 4))