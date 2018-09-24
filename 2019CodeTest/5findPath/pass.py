from itertools import groupby
from copy import deepcopy
import sys
sys.setrecursionlimit(10**6)

def findElementsInRange(candidates, start, end):
    for index, (x, y) in candidates:
        if start <= x and x <= end:
            return (index, (x, y))
    return (-1, (-1, -1))

def dfs(index, xVal, start, end, yIndexes):
    global dictByY, binaryTree
    
    # base case : end of branch
    if len(yIndexes) == 0:
        return
    
    nextLevelY = max(yIndexes)
    nextLevels = dictByY[nextLevelY]

    (lNode, (lX, lY)) = findElementsInRange(nextLevels, start, xVal)
    (rNode, (rX, rY)) = findElementsInRange(nextLevels, xVal, end)
    
    binaryTree[index] = (lNode, rNode)
    
    if lNode != -1 :
        newYIndexes = deepcopy(yIndexes)
        newYIndexes.remove(nextLevelY)
        dfs(lNode, lX, start, xVal, newYIndexes)
    if rNode != -1 :
        newYIndexes = deepcopy(yIndexes)
        newYIndexes.remove(nextLevelY)
        dfs(rNode, rX, xVal, end, newYIndexes)

def pre(i, orderList):
    global binaryTree
    
    # base case - leaf (not exist in binaryTree as key)
    if i not in binaryTree:
        orderList.append(i + 1)

    # not base case
    else :
        (left, right) = binaryTree[i]
        orderList.append(i + 1)
        if left != -1:
            pre(left, orderList)
        if right != -1:
            pre(right, orderList)

def post(i, orderList):
    global binaryTree
    
    # base case - leaf (not exist in binaryTree as key)
    if i not in binaryTree:
        orderList.append(i + 1)

    # not base case
    else :
        (left, right) = binaryTree[i]
        if left != -1:
            post(left, orderList)
        if right != -1:
            post(right, orderList)
        orderList.append(i + 1)
    
def solution(nodeinfo):
    global dictByY, binaryTree
    # setup dictByY
    numbered = list(enumerate(nodeinfo))
    sortByY = sorted(numbered, key = lambda e: e[1][1])
    groupByY = groupby(sortByY, lambda e:e[1][1])
    dictByY = dict(map(lambda x: (x[0],list(x[1])), groupByY))
    
    # initialize
    binaryTree = {}
    
    # find root
    rootY = max(dictByY)
    (rootIndex,(rootX, rootY)) = dictByY[rootY][0]
    
    # make ys
    ys = set(map(lambda x:x[1], nodeinfo))
    ys.remove(rootY)
    
    # dfs
    dfs(rootIndex, rootX, 0, 100000, ys)
    
    # print(binaryTree)
    
    preorder = []
    pre(rootIndex, preorder)
    
    postorder = []
    post(rootIndex, postorder)
    
    # print([preorder, postorder])
    
    answer = [preorder, postorder]
    return answer
