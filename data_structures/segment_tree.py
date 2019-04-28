class SegmentTree:
    arr = []
    tree = []

    def __init__(self, arr):
        self.arr = arr
        size = 4 * len(arr)
        self.tree = [0] * size

    def build_tree(self, node, tree_start, tree_end):
        if tree_start == tree_end:
            self.tree[node] = self.arr[tree_start]

            return

        mid = (tree_start + tree_end) // 2
        left = 2 * node
        right = left + 1

        self.build_tree(left, tree_start, mid)
        self.build_tree(right, mid + 1, tree_end)
        self.tree[node] = self.tree[left] + self.tree[right]

    def query(self, node, tree_start, tree_end, range_start, range_end):
        """
        :param node: the tree node that stores information of the range [tree_start, tree_end]
        :param tree_start: the start index of the range of this node
        :param tree_end: the end index of the range of this node
        :param range_start: the start index of the query range
        :param range_end: the end index of the query range
        :return: the sum of all elements in the range [range_start, range_end]
        """
        if range_start > tree_end or range_end < tree_start:
            return 0

        if tree_start >= range_start and tree_end <= range_end:
            return self.tree[node]

        mid = (tree_start + tree_end) // 2
        left = 2 * node
        right = left + 1

        return self.query(left, tree_start, mid, range_start, range_end) \
               + self.query(right, mid + 1, tree_end, range_start, range_end)

    def update(self, node, tree_start, tree_end, range_start, range_end, value):
        """
        Some description...
        :param node:
        :param tree_start:
        :param tree_end:
        :param range_start:
        :param range_end:
        :param value:
        :return:
        """
        if range_start > tree_end or range_end < tree_start:
            return 0

        if tree_start == tree_end:
            self.tree[node] += value

            return

        mid = (tree_start + tree_end) // 2
        left = 2 * node
        right = left + 1

        self.update(left, tree_start, mid, range_start, range_end, value)
        self.update(right, mid + 1, tree_end, range_start, range_end, value)
        self.tree[node] = self.tree[left] + self.tree[right]
