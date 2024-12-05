def parse_rules(filename):
    # Reads the page ordering rules from the file and returns them as a list of tuples
    rules = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by '|' and convert to integers
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
    return rules

def parse_updates(filename):
    updates = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by ',' and convert to integers
            updates.append(list(map(int, line.strip().split(','))))
    return updates

def build_graph(rules, pages):
    from collections import defaultdict
    graph = defaultdict(set)
    for x, y in rules:
        if x in pages and y in pages:
            graph[x].add(y)
    return graph

def topological_sort(graph, pages):
    from collections import deque
    
    indegree = {node: 0 for node in pages}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    queue = deque([node for node in pages if indegree[node] == 0])
    sorted_list = []
    
    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_list if len(sorted_list) == len(pages) else None

def is_correct_order(update, rules):
    graph = build_graph(rules, update)
    sorted_order = topological_sort(graph, update)
    return sorted_order == update

def main():
    # Parse the rules from the file
    rules = parse_rules('pages_ordering_rules.txt')
    
    # Parse the updates from the file
    updates = parse_updates('pages_to_produce_in_each_update.txt')
    
    # Check each update for correct order
    for update in updates:
        if is_correct_order(update, rules):
            print(f"Update {update} is in correct order.")
        else:
            print(f"Update {update} is NOT in correct order.")

if __name__ == "__main__":
    main()