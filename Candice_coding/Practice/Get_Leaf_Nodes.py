class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = []

def getLeafNodes(treeNode):
    '''Given a treeNode, return all the leaf nodes belong to this treeNode'''
    if not treeNode:
        return []
    if not treeNode.children:
        return [treeNode.val]
    result = []
    for child in treeNode.children:
        leaf = getLeafNodes(child)
        if leaf:
            result.extend(leaf)
    return result


if __name__ == '__main__':
    food = TreeNode('food')
    america = TreeNode('america')
    china = TreeNode('china')
    mexico = TreeNode('mexico')
    india = TreeNode('india')
    food.children = [america, china, mexico, india]
    mifan = TreeNode('mifan')
    mianshi = TreeNode('mianshi')
    china.children = [mifan, mianshi]
    jiaozi = TreeNode('jiaozi')
    baozi = TreeNode('baozi')
    mianshi.children = [jiaozi, baozi]
    gali = TreeNode('gali')
    india.children = [gali]
    print getLeafNodes(food)