import copy


class Node:
    def __init__(self, node_type=None, row=None, col=None):
        self.node_type = node_type
        self.NW = None
        self.NE = None
        self.SE = None
        self.SW = None
        self.row = row
        self.col = col

    def init_children(self):
        self.node_type = 'G'
        self.NW = Node()
        self.NE = Node()
        self.SE = Node()
        self.SW = Node()

    def color(self):
        if self.node_type == "G":
            return "GRAY"

        elif self.node_type == 1:
            return "BLACK"

        else:
            return "WHITE"


def build_tree(r, image, cur_col, cur_row, L, block_num, display_output=True):

    cur_block = image[cur_row:cur_row + L, cur_col:cur_col + L]
    # print(cur_block)

    if L == 1:
        r.node_type = image[cur_row][cur_col]
        return r

    else:
        color = image[cur_row][cur_col]

        for i, _ in enumerate(cur_block):
            for j, _ in enumerate(cur_block[i]):
                if cur_block[i][j] != color:
                    r.init_children()
                    if display_output and r.node_type == 'G':
                        print(f"\tFOUND pixel with different value at {j + 1 + cur_col, i + 1 + cur_row}")  # nopep8
                        print(f"\tSPLIT block {block_num}")

                    r.NW = build_tree(r.NW, image, cur_col, cur_row, L//2, (4 * block_num) + 1, display_output)  # nopep8
                    r.NE = build_tree(r.NE, image, cur_col + (L//2), cur_row, L//2, (4 * block_num) + 2, display_output)  # nopep8
                    r.SW = build_tree(r.SW, image, cur_col, cur_row + (L//2), L//2, (4 * block_num) + 3, display_output)  # nopep8
                    r.SE = build_tree(r.SE, image, cur_col + (L//2), cur_row + (L//2), L//2, (4 * block_num) + 4, display_output)  # nopep8
                    return r
        r.node_type = color
        return r


def preorder(n, block_num):
    if not n:
        return
    else:
        if n.__children is None:
            node_type = 'LEAF'
        else:
            node_type = 'INTERNAL'
        print(f"\t {block_num} {node_type}")
        preorder(n.NW, (4 * block_num) + 1)
        preorder(n.NE, (4 * block_num) + 2)
        preorder(n.SW, (4 * block_num) + 3)
        preorder(n.SE, (4 * block_num) + 4)


def intersection(s, t, q, block_num):

    if s.node_type == 0 or t.node_type == 0:
        q = Node(0)
        print(f"\t{block_num} {s.color()} {t.color()} {q.color()}")  # nopep8

    elif s.node_type == 1:
        q = copy.deepcopy(t)
        print(f"\t{block_num} {s.color()} {t.color()} {q.color()}")  # nopep8
    elif t.node_type == 1:
        q = copy.deepcopy(s)
        print(f"\t{block_num} {s.color()} {t.color()} {q.color()}")  # nopep8

    else:
        q = Node()
        q.init_children()
        print(f"\t{block_num} {s.color()} {t.color()} {q.color()}")  # nopep8
        q.NW = intersection(s.NW,  t.NW, q.NW, (4 * block_num) + 1)
        q.NE = intersection(s.NE,  t.NE, q.NE, (4 * block_num) + 2)
        q.SW = intersection(s.SW,  t.SW, q.SW, (4 * block_num) + 3)
        q.SE = intersection(s.SE,  t.SE, q.SE, (4 * block_num) + 4)

        if q.NW.node_type == 0 and q.NE.node_type == 0 and q.SW.node_type == 0 and q.SE.node_type == 0:
            q.node_type = 0
            q.NW = None
            q.NE = None
            q.SW = None
            q.SE = None
            print(f"\t{block_num} {s.color()} {t.color()} {q.color()}")  # nopep8

    return q
