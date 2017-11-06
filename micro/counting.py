import numpy as np


def count_objects(img):
    ny, nx = img.shape
    E = 0
    I = 0
    for i in range(nx-1):
        for j in range(ny-1):
            if external_match(img[i:i+2, j:j+2]):
                E += 1
            if internal_match(img[i:i+2, j:j+2]):
                I += 1
    return (E - I)/4

def external_match(a):
    """
    Checks if the given 2-by-2 array "a"
    is equal to any one of the following:

    a) 0 0  b) 0 0
       0 1     1 0

    c) 1 0  c) 0 1
       0 0     0 0

    If a match is found, then `True` is returned.
    Otherwise, `False` is returned.

    Parameters
    ----------

    a : array_like (size: [2, 2])
        A 2-by-2 binary array

    Returns
    -------

    True or False
    """
    # ------ YOUR CODE HERE ------ #
    b = []
    b.append([[0,0],[0,1]])
    b.append([[0,0],[1,0]])
    b.append([[1,0],[0,0]])
    b.append([[0,1],[0,0]])

    for i in range(len(a)-1):
        if np.all(b[i]==a):
            return True
    return False
    

    # ---------------------------- #


def internal_match(a):
    """
    Checks if the given 2-by-2 array "a"
    is equal to any one of the following:

    a) 1 1  b) 1 1
       1 0     0 1

    c) 0 1  c) 1 0
       1 1     1 1

    If a match is found, then `True` is returned.
    Otherwise, `False` is returned.

    Parameters
    ----------

    a : array_like (size: [2, 2])
        A 2-by-2 binary array

    Returns
    -------

    True or False
    """
    # ------ YOUR CODE HERE ------ #
    b = []
    b.append([[1,1],[1,0]])
    b.append([[1,1],[0,1]])
    b.append([[0,1],[1,1]])
    b.append([[1,0],[1,1]])

    for i in range(len(a)-1):
        if np.all(b[i] == a):
            return True

    return False 

    # ---------------------------- #
