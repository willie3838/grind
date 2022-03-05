import random

def random_subset(n, k):
    changed = {}
    for i in range(k):
        rdm_idx = random.randrange(i,n)
        i_mapped = changed.get(i,i)
        rand_mapped = changed.get(rdm_idx, rdm_idx)
        changed[rdm_idx] = i_mapped
        changed[i] = rand_mapped
   
    return [changed[i] for i in range(k)]
    
print(random_subset(3, 2))