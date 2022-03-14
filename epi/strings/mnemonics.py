
# TC: O(4^n * n) SC: O(4^n)
def phoneNumber(digits):
    mapp = {
        "2":"ABC",
        "3":"DEF",
        "4":"GHI",
        "5":"JKL",
        "6":"MNO",
        "7":"PQRS",
        "8":"TUV",
        "9":"WXYZ"
    }
    res = []
    search(digits, mapp, "", res)
    return res

def search(digits, mapp, path, res):
    if not digits:
        res.append(path)
        return

   
    if digits[0] in mapp:
        for char in mapp[digits[0]]:
            search(digits[1:], mapp, path+char, res)
    else:
        search(digits[1:], mapp, path, res)

print(phoneNumber("2276696"))