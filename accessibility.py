class Node():
    def __init__(self, ID):
        self.ID = ID
        self.neighs = []
        self.weights = []
        self.is_trans = False
        self.route = []


def dfs(start, cur, w_so_far):
    global res
    for n, w in zip(cur.neighs, cur.weights):
        if n in visited or w_so_far + w > 5:
            continue
        
        visited.add(n)
        _w_so_far = w_so_far + w
        try:
            res[start.ID].append((n.ID, _w_so_far))
        except KeyError:
            res[start.ID] = [(n.ID, _w_so_far)]

        dfs(start, n, _w_so_far)

    return None


if __name__ == "__main__":
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = \
        Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9), Node(10), Node(11)
    
    n1.neighs = [n2, n5]
    n1.weights = [2, 1]
    n1.is_trans = True
    n2.neighs = [n3]
    n2.weights = [2]
    n3.neighs = []
    n3.weights = []
    n4.neighs = [n1]
    n4.weights = [3]
    n5.neighs = [n6, n11]
    n5.weights = [3, 0]
    n6.neighs = [n7, n10]
    n6.weights = [4, 1]
    n6.is_trans = True
    n7.neighs = []
    n7.weights = []
    n8.neighs = [n6]
    n8.weights = [3]
    n9.neighs = [n1]
    n9.weights = [2]

    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

    visited = set()
    t = 5
    res = {}
    for n in nodes:
        dfs(n, n, 0)
        visited = set()
    print(res)
        


    

