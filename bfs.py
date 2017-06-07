import unittest


def bfs(tree, key):
    """
    Breadth First Search
    """

    queue = [tree[0]]

    while queue:
        current_node = queue.pop(0)

        if current_node['key'] == key:
            return current_node

        children = current_node['children']
        for child in children:
            queue.append(child)


class TestBFS(unittest.TestCase):
    """
    Unit Tests
    """
    tree = [
        {
            "key": 1,
            "children": [
                {
                    "key": 2,
                    "children": [
                        {
                            "key": 5,
                            "children": [
                                {
                                    "key": 9,
                                    "children": []
                                },
                                {
                                    "key": 10,
                                    "children": []
                                }
                            ]
                        },
                        {
                            "key": 6,
                            "children": []
                        }
                    ]
                },
                {
                    "key": 3,
                    "children": []
                },
                {
                    "key": 4,
                    "children": [
                        {
                            "key": 7,
                            "children": [
                                {
                                    "key": 11,
                                    "children": []
                                },
                                {
                                    "key": 12,
                                    "children": []
                                }
                            ]
                        },
                        {
                            "key": 8,
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]

    def test_bfs_root_node_search_returns_entire_tree(self):
        """
        Test search for first key returns the root node.
        """
        self.assertEqual(bfs(self.tree, 1), self.tree[0])

    def test_bfs_returns_correct_nodes(self):
        """
        Test different keys return correct nodes
        """
        
        self.assertEqual(bfs(self.tree, 3), {"key": 3, "children": []})
        self.assertEqual(bfs(self.tree, 4), {"key": 4, "children": [{"key": 7, "children": [ {"key": 11, "children": []}, {"key": 12, "children": []}]}, {"key": 8, "children": []}]})
        self.assertEqual(bfs(self.tree, 4), {"key": 4, "children": [{"key": 7, "children": [ {"key": 11, "children": []}, {"key": 12, "children": []}]}, {"key": 8, "children": []}]})
        self.assertEqual(bfs(self.tree, 9), {"key": 9, "children": []})


if __name__ == '__main__':
    unittest.main()
