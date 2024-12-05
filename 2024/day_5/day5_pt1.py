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
    # Reads the update lists from the file and returns them as a list of lists
    updates = []
    with open(filename, 'r') as f:
        for line in f:
            # Split each line by ',' and convert to a list of integers
            updates.append(list(map(int, line.strip().split(','))))
    return updates

def build_graph(rules, pages):
    from collections import defaultdict
    # Constructs a directed graph only using rules relevant to the given pages
    graph = defaultdict(set)
    for x, y in rules:
        if x in pages and y in pages:
            # Add a directed edge from x to y
            graph[x].add(y)
    return graph

def topological_sort(graph, pages):
    from collections import deque
    
    # Initialize indegree of all pages to 0
    indegree = {node: 0 for node in pages}
    for node in graph:
        for neighbor in graph[node]:
            # Increase indegree for each neighbor
            indegree[neighbor] += 1
    
    # Initialize queue with nodes having 0 indegree
    queue = deque([node for node in pages if indegree[node] == 0])
    sorted_list = []
    
    while queue:
        node = queue.popleft()
        sorted_list.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            # If indegree becomes 0, add to queue
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Return sorted list if it contains all pages, otherwise None
    return sorted_list if len(sorted_list) == len(pages) else None

def is_correct_order(update, rules):
    # Check if the given update is in correct order according to the rules
    graph = build_graph(rules, update)
    sorted_order = topological_sort(graph, update)
    # Return true if the update matches the topological sort order
    return sorted_order == update

def find_middle_page(update):
    # Return the middle page of the update list
    length = len(update)
    return update[length // 2]

def main():
    # Parse rules and updates from files
    rules = parse_rules('pages_ordering_rules.txt')
    updates = parse_updates('pages_to_produce_in_each_update.txt')
    
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