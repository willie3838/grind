'''
/usr/lib/./gross = /usr/lib/gross
/usr/lib/../bin = /usr/bin
'''

def normalize(path):
    path = path.split("/")
    res = []

    for x in path:
        if x != "":
            if x == "..":
                # if it's empty we can't go any further anyways...
                if res:
                    res.pop()
            # if it's . we don't do anything anyways
            elif x != ".":
                res.append(x)
    
    
    res = "/" + "/".join(res)
    
    return res

print(normalize("/usr/lib/./gross"))
print(normalize("/usr/lib/../gross"))
print(normalize("../.."))
print(normalize("./"))