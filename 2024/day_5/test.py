def parse_rules(filename):
    # Reads the page ordering rules from the file and returns them as a list of tuples
    print(f"Parsing rules from {filename}")
    rules = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by '|' and convert to integers
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
            print(f"Rule parsed: {x} -> {y}")
    print(f"Total rules parsed: {len(rules)}")
    return rules

def parse_updates(filename):
    # Reads the update lists from the file and returns them as a list of lists
    print(f"Parsing updates from {filename}")
    updates = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by ',' and convert to a list of integers
            update = list(map(int, line.strip().split(',')))
            updates.append(update)
            print(f"Update parsed: {update}")
    print(f"Total updates parsed: {len(updates)}")
    return updates

def build_graph(rules, pages):
    from collections import defaultdict
    # Constructs a directed graph only using rules relevant to the given pages
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
    for node in graph:
        for neighbor in graph[node]:
            # Increase indegree for each neighbor
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
            # If indegree becomes 0, add to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)
                print(f"Node {neighbor} added to queue")
    
    print(f"Topologically sorted list: {sorted_list}")
    
    # Return sorted list if it contains all pages, otherwise None
    return sorted_list if len(sorted_list) == len(pages) else None

def is_correct_order(update, rules):
    # Check if the given update is in correct order according to the rules
    print(f"Checking order for update: {update}")
    graph = build_graph(rules, update)
    sorted_order = topological_sort(graph, update)
    is_correct = sorted_order == update
    print(f"Update {update} is {'correctly' if is_correct else 'not'} ordered.")
    return is_correct

def find_middle_page(update):
    # Return the middle page of the update list
    length = len(update)
    middle_page = update[length // 2]
    print(f"Middle page of {update} is {middle_page}")
    return middle_page

def main():
    # Parse rules and updates from files
    rules = parse_rules('test_pages_ordering_rules.txt')
    updates = parse_updates('test_pages_to_produce_in_each_update.txt')
    
    sum_of_middle_pages = 0
    
    # Process each update
    for update in updates:
        if is_correct_order(update, rules):
            # If correctly ordered, find and add the middle page to sum
            middle_page = find_middle_page(update)
            sum_of_middle_pages += middle_page
    
    # Print the total sum of middle pages of correctly ordered updates
    print("Sum of middle pages of correctly ordered updates:", sum_of_middle_pages)

if __name__ == "__main__":
    main()