'''
19216811


                TREE
            1.  19.   192. 

TC: O(3^4 * 12) <- we break off into three branches and at most we'll have a height of 4 in the tree
SC: O(3^4)
'''
def allValid(ip):
    res = []
    search(ip, res, "", 3)
    return res

def search(ip, res, path, periods):
    if periods < 0:
        return
    if not periods and int(ip) <= 255 and (ip[0] != "0" or len(ip) == 1):
        res.append(path+ip)
        return

    for i in range(len(ip)-1):
        if int(ip[:i+1]) <= 255 and (ip[0] != "0" or i==0):
            search(ip[i+1:], res, path + ip[:i+1] + ".", periods-1)
print(allValid("19216811"))