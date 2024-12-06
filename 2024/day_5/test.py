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
    # Create a graph using a defaultdict where each key has an empty set as a default value
    graph = defaultdict(set)
    print(f"Building graph for pages: {pages}")
    for x, y in rules:
        if x in pages and y in pages:
            # Add a directed edge from x to y
            graph[x].add(y)
            print(f"Adding edge: {x} -> {y}")
    print(f"Constructed graph: {dict(graph)}")
    return graph

def topological_sort(graph, pages):
    from collections import deque
    # Initialize indegree of all pages to 0
    indegree = {node: 0 for node in pages}
    
    # Calculate the indegree for each node
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    
    print(f"Initial indegrees: {indegree}")
    
    # Initialize queue with nodes having 0 indegree
    queue = deque([node for node in pages if indegree[node] == 0])
    sorted_list = []
    
    print(f"Starting nodes (indegree 0): {list(queue)}")
    
    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        print(f"Processing node: {node}")
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            print(f"Decreased indegree of {neighbor} to {indegree[neighbor]}")
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                print(f"Node {neighbor} added to queue")
    
    print(f"Topologically sorted list: {sorted_list}")
    
    # Return sorted list if it contains all pages, otherwise None
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
            # Visualize the correction process
            graph = build_graph(rules, update)
            correct_order = topological_sort(graph, update)
            print(f"Correct order: {correct_order}")

if __name__ == "__main__":
    main()