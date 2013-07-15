## Task 2
def dict2list(dct, keylist): return [ dct[key] for key in keylist]
# def dict2list(dct, keylist): pass

def list2dict(L, keylist): return { key:value for key,value in zip(keylist,L)} 
# def list2dict(L, keylist): pass

## Task 3
def listrange2dict(L):
    """
    Input: a list
    Output: a dictionary that, for i = 0, 1, 2, . . . , len(L), maps i to L[i]

    You can use list2dict or write this from scratch
    """
    return {xx:L[xx] for xx in range(len(L))}