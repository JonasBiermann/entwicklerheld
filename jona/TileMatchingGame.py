import copy
import numpy as np
from typing import List


def calculate(initial_state: np.ndarray) -> List[np.ndarray]:
    a = initial_state.tolist()
    finilst = []
    h = -1
    while len(finilst) > h:
        def search(tmp1, lst, i, j):
            if lst[i][j] > 0 and [i, j] not in tmp1:
                tmp1 += [[i, j]]
                if i-1 >= 0:  # over
                    if lst[i-1][j] == lst[i][j] and [i-1, j] not in tmp1:
                        search(tmp1, lst, i-1, j)

                if i+1 < 5:  # under
                    if lst[i+1][j] == lst[i][j] and [i+1, j] not in tmp1:
                        search(tmp1, lst, i+1, j)

                if j+1 < 5:  # right
                    if lst[i][j+1] == lst[i][j] and [i, j+1] not in tmp1:
                        search(tmp1, lst, i, j+1)

                if j-1 >= 0:  # left
                    if lst[i][j-1] == lst[i][j] and [i, j-1] not in tmp1:
                        search(tmp1, lst, i, j-1)
                return(tmp1)

        tmp = []
        for i in range(5):
            for j in range(5):
                p = search([], a, i, j)
                if type(p) == list:
                    if len(p) >= 3:
                        tmp += [p]
        for i in range(len(tmp)):
            tmp[i].sort()

        res = []
        for i in tmp:
            if i not in res:
                res.append(i)

        for i in range(len(res)):
            for j in res[i]:
                a[j[0]][j[1]] = 0

        if a not in finilst:
            finilst.append(copy.deepcopy(a))
        h += 1

        for i in range(len(res)):
            for j in res[i]:
                a[j[0]][j[1]] = 9

        x = 0
        for i in range(4, 0, -1):
            for j in range(5):
                while a[i][j] == 9:
                    while x < i:
                        y = a[x+1][j]
                        if x == 0:
                            a[x+1][j] = a[x][j]
                        else:
                            a[x+1][j] = z
                        z = y
                        x += 1
                    x = 0
                    a[0][j] = 0

        if a not in finilst:
            finilst.append(copy.deepcopy(a))
        h += 1

    return finilst
