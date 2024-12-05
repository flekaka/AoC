def parse_rules(filename):
    rules = []
    with open(filename, 'r') as f:
        for line in f:
            x, y = map(int, line.strip().split('|'))
            rules.append((x, y))
    return rules

def parse_updates(filename):
    updates = []
    with open(filename, 'r') as f:
        for line in f:
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

def find_middle_page(update):
    length = len(update)
    return update[length // 2]

def reorder_update(update, rules):
    # Build the graph and get the topological sort for the update
    graph = build_graph(rules, update)
    sorted_order = topological_sort(graph, update)
    return sorted_order

def main():
    rules = parse_rules('pages_ordering_rules.txt')
    updates = parse_updates('pages_to_produce_in_each_update.txt')
    
    sum_of_middle_pages_incorrect = 0
    
    for update in updates:
        if not is_correct_order(update, rules):
            # Reorder the update and find the middle page
            correct_order = reorder_update(update, rules)
            if correct_order:  # Ensure the sorting is successful
                middle_page = find_middle_page(correct_order)
                sum_of_middle_pages_incorrect += middle_page
    
    print("Sum of middle pages of correctly reordered updates:", sum_of_middle_pages_incorrect)

if __name__ == "__main__":
    main()