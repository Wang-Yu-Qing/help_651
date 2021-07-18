class Node():
    def __init__(self, ID, route, is_transfer):
        self.ID = ID
        self.neighs = []
        self.weights = []
        self.routes = []
        self.route = route
        self.is_transfer = is_transfer


def dfs(start, cur_station, cur_route, w_so_far, trans_so_far):
    """
        @start: start station (station to compute accessibility)
        @cur_station: station to reach for the current step
        @cur_route: the route taken to reach the current station
        @w_so_far: the total weights needed to reach the current station
        @trans_so_far: the total transfer times needed to reach the current station
    """
    global res, searched, MAX_W, MAX_TRANSFER
    # check if we can reach this station
    if cur_station.ID in searched or w_so_far > MAX_W or trans_so_far > MAX_TRANSFER:
        return

    # if we are here, cur_station is valid
    searched.add(cur_station.ID)
    try:
        res[start.ID].append((cur_station.ID, w_so_far))
    except KeyError:
        res[start.ID] = [(cur_station.ID, w_so_far)]

    # so let's begin searching from cur_station
    for next_station, weight, route in zip(cur_station.neighs, cur_station.weights, cur_station.routes):
        if route != cur_route and not cur_station.is_transfer:
            # we need transfer to reach the next station
            dfs(start, next_station, route, w_so_far + weight, trans_so_far + 1)
        else:
            # we don't need transfer to reach the next station
            dfs(start, next_station, route, w_so_far + weight, trans_so_far)


if __name__ == "__main__":
    """
        1 : [(2, 2), (3, 4), (12, 2), (5, 1), (6, 4), (10, 5), (11, 1)] 
        2 : [(3, 2), (12, 0)] 
        4 : [(1, 3), (2, 5), (12, 5), (5, 4), (11, 4)] 
        5 : [(6, 3), (10, 4), (11, 0)] 
        6 : [(7, 4), (10, 1)] 
        8 : [(6, 3), (10, 4)] 
        9 : [(1, 2), (2, 4), (12, 4), (5, 3), (11, 3)]
    """
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
        
