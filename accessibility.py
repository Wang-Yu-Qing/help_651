class Node():
    def __init__(self, ID, route, is_transfer):
        self.ID = ID
        self.neighs = []
        self.weights = []
        self.routes = []
        self.route = route
        self.is_transfer = is_transfer


def dfs(start, cur_station, cur_route, w_so_far, trans_so_far):
    global res, searched, MAX_W, MAX_TRANSFER
    for n, w, r in zip(cur_station.neighs, cur_station.weights, cur_station.routes):
        # update trans so far and current route 
        # if reach station n needs transfer
        if r != cur_route and not cur_station.is_transfer:
            _trans_so_far = trans_so_far + 1
            _cur_route = r
        else:
            _trans_so_far = trans_so_far
            _cur_route = cur_route

        # update weights so far if reach station n
        _w_so_far = w_so_far + w

        # check if this potential next station is valid
        if n.ID in searched or _w_so_far > MAX_W or _trans_so_far > MAX_TRANSFER:
            continue
        
        # if reach here, the n is a valid reach station
        searched.add(n.ID)

        # add n to valid reach station
        try:
            res[start.ID].append((n.ID, _w_so_far))
        except KeyError:
            res[start.ID] = [(n.ID, _w_so_far)]

        # search from station n
        dfs(start, n, _cur_route, _w_so_far, _trans_so_far)

    return None


if __name__ == "__main__":
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12 = \
        Node(1, "A,B", True), Node(2, "A,E", True), Node(3, "A", False), \
        Node(4, "A", False), Node(5, "B", False), Node(6, "B,D", True), \
        Node(7, "D", False), Node(8, "D", False), Node(9, "B", False), \
        Node(10, "B", False), Node(11, "C", False), Node(12, "E", False)
    
    n1.neighs, n1.weights, n1.routes = [n2, n5], [2, 1], ["A", "B"]
    n2.neighs, n2.weights, n2.routes = [n3, n12], [2, 0], ["A", "E"]
    n4.neighs, n4.weights, n4.routes = [n1], [3], ["A"]
    n5.neighs, n5.weights, n5.routes = [n6, n11], [3, 0], ["B", "C"]
    n6.neighs, n6.weights, n6.routes = [n7, n10], [4, 1], ["D", "B"]
    n8.neighs, n8.weights, n8.routes = [n6], [3], ["D"]
    n9.neighs, n9.weights, n9.routes = [n1], [2], ["B"]

    nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]

    searched = set()
    MAX_W = 5
    MAX_TRANSFER = 1
    res = {}

    # start search
    for n in nodes:
        dfs(n, n, n.route.split(",")[0], 0, 0)
        searched = set()

    # print result
    for k, v in res.items():
        print(k, ": ")
        print(v)
        
