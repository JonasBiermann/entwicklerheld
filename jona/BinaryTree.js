export function printTree(treeNode) {
    function toArray(obj) {
        obj = Object.values(obj)
        if (obj[1] != null) {
            obj[1] = toArray(obj[1])
        }
        if (obj[2] != null) {
            obj[2] = toArray(obj[2])
        }
        return obj
    }
    return toArray(treeNode)
}

export function checkTreeEqualness(treeNode1, treeNode2) {
    if (printTree(treeNode1).toString() == printTree(treeNode2).toString()) {
        return true
    }
    else {
        return false
    }
}

export function reverse(treeNode) {
    if (treeNode["left"] != null && treeNode["right"] != null) {
        console.log(treeNode.left)
        let tmp = treeNode.left
        treeNode.left = treeNode.right
        treeNode.right = tmp
        reverse(treeNode.left)
        reverse(treeNode.right)
    }
    console.log(treeNode)
    return treeNode
}