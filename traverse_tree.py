class Node():
    def __init__(self, id):
        self.id = id
        self.l = None
        self.r = None

#  tree:
#                 3
#         10              2
#     7       5               4
# 0                               9

root = Node(3)
n10, n2, n7, n5, n4, n0, n9 = \
    Node(10), Node(2), Node(7), Node(5), Node(4), Node(0), Node(9)
root.l = n10
root.r = n2
n10.l = n7
n10.r = n5
n7.l = n0
n2.r = n4
n4.r = n9


# ----- pre-order:
def pre(n):
    if not n:
        return
    print(n.id, end=" -> ")
    pre(n.l)
    pre(n.r)

pre(root)
print()
# 3 -> 10 -> 7 -> 0 -> 5 -> 2 -> 4 -> 9


# ----- middle-order:
def middle(n):
    if not n:
        return
    middle(n.l)
    print(n.id, end=" -> ")
    middle(n.r)

middle(root)
print()
# 0 -> 7 -> 10 -> 5 -> 3 -> 2 -> 4 -> 9


# ----- last-order:
def last(n):
    if not n:
        return
    last(n.l)
    last(n.r)
    print(n.id, end=" -> ")

last(root)
print()
# 0 -> 7 -> 5 -> 10 -> 9 -> 4 -> 2 -> 3
