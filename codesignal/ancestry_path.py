class Node:
    """
    Used to build a tree.
    """

    def __init__(self, name, children=[]):
        self.children = children
        self.name = name

def create_tree():
    """
    Creates the example tree below:
    
               1
             / | \
            /  |  \         
           2   3   4
         / |   |   | \
        /  |   |   |  \        
       5   6   7   8   9
         /   / |   |     \
        /   /  |   |      \
       10  11  12  13     14
    """
    return Node(
        1,
        [
            Node(2, [Node(5), Node(6, [Node(10)])]),
            Node(3, [Node(7, [Node(11), Node(12)])]),
            Node(4, [Node(8, [Node(13)]), Node(9, [Node(14)])]),
        ],
    )

def ancestry_path(target_node_name, node):
    """
    Given a Node (the root Node in a tree) and the name of a target Node, determine the
    ancestry path from the root Node to the Node with the specified name (returned as a
    list). You may assume that Node names in the tree are unique.

    Use the create_tree() method defined above to test your code. You may create
    additional trees to further test your code, but this is not required.

    See test_ancestry_path_example for an example of how your code will be executed.
    """

    if not node:
        return []
    
    if node.name == target_node_name:
        return [target_node_name]
    
    res = []
    for child in node.children:
        path = ancestry_path(target_node_name, child)
        if len(path) >= 1:
            return [node.name] + path

    return res


ancestry_path(11, create_tree())