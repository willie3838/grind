import random

def sample(arr, k):
    sampling_results = list(arr[:k])
    seen_so_far = k
    
    for x in arr:
        seen_so_far += 1
        # we dont do just 0,k b/c we need the % to be uniformily random
        # we know it's uniformly random because each time we generate the subset
        # the probability is proportionate to the size of the array, making it equally likely
        replace = random.randrange(seen_so_far)
        if replace < k:
            sampling_results[replace] = x
    return sampling_results