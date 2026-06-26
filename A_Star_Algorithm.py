import heapq
def a_star(start, goal, graph, heuristic):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return list(reversed(path)), cost_so_far[goal]
        for neighbor, cost in graph.get(current, {}).items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic.get(neighbor, float('inf'))
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return None, float('inf')
if __name__ == '__main__':
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 3, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    heuristic = {'A': 7,'B': 6,'C': 2,'D': 0}
    path, cost = a_star('A', 'D', graph, heuristic)
    print('Path:', path)
    print('Cost:', cost)