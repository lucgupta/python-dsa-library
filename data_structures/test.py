from segment_tree import *

arr = [6, 4, 3, 2, 13, 8, 5, 15]

segment_tree = SegmentTree(arr)
length = len(arr)

segment_tree.build_tree(1, 0, length - 1)

print(segment_tree.tree)

arr_start = 1
arr_end = 4

print(segment_tree.query(1, 0, length - 1, arr_start, arr_end))

value = 5
segment_tree.update(1, 0, length - 1, arr_start, arr_end, value)

print(segment_tree.tree)
