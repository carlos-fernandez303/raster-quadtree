import sys
import numpy as np
from quadtree import *


with open(sys.argv[1]) as image_file:
    k = int(next(image_file))

    image = []
    for line in image_file:
        image.append([int(x) for x in line.split()])

image = np.array(image)

root_1 = Node()
root_1.node_type = image[0][0]


print("\nSTART INPUT\n")
build_tree(root_1, image, 0, 0, k, 0)
print("\nSPLIT COMPLETED\n\n")
print("START RQ\n")
preorder(root_1, 0)
print("\nEND RQ\n")
