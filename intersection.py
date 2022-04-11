import sys
import numpy as np
from quadtree import *

with open(sys.argv[1]) as image_file:
    k1 = int(next(image_file))

    image = []
    for line in image_file:
        image.append([int(x) for x in line.split()])

image_1 = np.array(image)

with open(sys.argv[2]) as image_file:
    k2 = int(next(image_file))

    image = []
    for line in image_file:
        image.append([int(x) for x in line.split()])

image_2 = np.array(image)

root_1 = Node()
root_1.node_type = image_1[0][0]
build_tree(root_1, image_1, 0, 0, k1, 0, False)

root_2 = Node()
root_2.node_type = image_2[0][0]
build_tree(root_2, image_2, 0, 0, k2, 0, False)

print("\nSTART INTERSECTION\n")
root_3 = intersection(root_1, root_2, None, 0)
print("\nEND INTERSECTION\n\n")

print("START RQ\n")
preorder(root_3, 0)
print("\nEND RQ\n")
