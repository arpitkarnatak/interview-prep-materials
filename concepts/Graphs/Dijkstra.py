def dijkstra(self, graph, start_node):
    costs = {node: float("inf") for node in graph}
    costs[start_node] = 0

    next_cheapest_node_to_reach = [(0, start_node)]

    while next_cheapest_node_to_reach:
        cost_to_reach, current_node = heapq.heappop(next_cheapest_node_to_reach)
        for neighbor in graph[current_node]:
            neighbor_node, cost = neighbor
            cost_to_reach_neighbor = cost + cost_to_reach

            if cost_to_reach_neighbor < costs[neighbor_node]:
                costs[neighbor_node] = cost_to_reach_neighbor
                heapq.heappush(next_cheapest_node_to_reach, (cost_to_reach_neighbor, neighbor_node))
            else:
                pass
    return costs