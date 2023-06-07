import random
import time

"""
This code provided is an AI of 24 game using depth-first search
Both sets of code generates a random set of 4 integers then goes
through a series of operations to try and reach the goal of 24.
Also, at the end it tells the processing time it took to find a solution 
if there is one.

"""
# This method generates a random list of 4 integers in range [1,13]
# @param values: an empty list originally
# @return values: a full list of 4 generated integers
def generate_start_nodes(values):
    while len(values) < 4:
        value = random.randint(1,13)
        values.append(value)
    return values


# This method finds the first solution and returns it with depth-first-search
# @params nodes: set of integers (probably wrong word to describe)
# @path_sequence: a sequence of strings where each string describes an action of a state
# @return: bool True or False
def single_solution_24_game(nodes,path_sequence):
    if len(nodes) == 1:
        if nodes[0] == 24:
            return True
        else:
            path_sequence.clear()
            return False
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                a = nodes[i]
                b = nodes[j]
                remaining_nodes = [nodes[k] for k in range(len(nodes)) if k != i and k != j]

                # Addition
                if single_solution_24_game([a + b] + remaining_nodes,path_sequence):
                    tuple = (str(a) + "add" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Subtraction
                if single_solution_24_game([a - b] + remaining_nodes,path_sequence):
                    tuple = (str(a) + "sub" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Multiplication
                if single_solution_24_game([a * b] + remaining_nodes,path_sequence):
                    tuple = (str(a) + "mu" + str(b))
                    path_sequence.append(tuple)
                    return True

                # Division
                if b != 0 and single_solution_24_game([a / b] + remaining_nodes,path_sequence):
                    tuple = (str(a) + "div" + str(b))
                    path_sequence.append(tuple)
                    return True

    return False  

#Main function that calls the functions above
def main():
    
    values = []
    path_sequence = []
    nodes = generate_start_nodes(values)
    print("FIRST PROGRAM: ")
    print("Input: ", nodes)
    start = time.time()
    if single_solution_24_game(nodes,path_sequence):
        print("Yes it does reach to 24")
        path_sequence.reverse()
        print("Found Solution:", path_sequence)

    else:
        print("It never reaches to 24")
    end = time.time()
    processing_time = (end - start) * 10**3
    print("Processing time: " + str(processing_time) + "ms")
    
main()

# Nested functions
# outer function contains the variable "path_solutions" to store paths
# that lead to goal value 24
# @param nodes : list of integers
# @return path_solutions : list of strings containing paths to solutions
def multiple_solutions_24_game(nodes):
    path_solutions = []
    
    # Similar function to one above except it does not return a boolean value
    # Stores solutions to the list in the outer function
    # @param nodes : list of integers
    # @param path_sequence: an initialised empty list

    def find_a_solution(nodes, path_sequence=[]):
        if len(nodes) == 1:
            if nodes[0] == 24:
                path_solutions.append(path_sequence)
            return
            
            
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j:
                    a = nodes[i]
                    b = nodes[j]
                    remaining_nodes = [nodes[k] for k in range(len(nodes)) if k != i and k != j]
            
                    # Addition
                    tuple = (str(a) + "add" + str(b))
                    find_a_solution([a + b] + remaining_nodes,path_sequence + [tuple])
                        

                    # Subtraction
                    tuple = (str(a) + "sub" + str(b))
                    #remaining_paths.append(tuple)
                    find_a_solution([a - b] + remaining_nodes,path_sequence + [tuple])
                        
                    # Multiplication
                    tuple = (str(a) + "mu" + str(b))
                    find_a_solution([a * b] + remaining_nodes,path_sequence + [tuple])
                        

                    # Division
                    if b != 0:
                        tuple = (str(a) + "div" + str(b))
                        #remaining_paths.append(tuple)
                        find_a_solution([a / b] + remaining_nodes,path_sequence + [tuple])
                        
    find_a_solution(nodes)
    return path_solutions

# Main function that generates start node then passes it on to the function above    
def main2():
    values = []
    nodes = generate_start_nodes(values)
    print("SECOND PROGRAM: ")
    print("Input: ", nodes)
    start = time.time()
    solutions = multiple_solutions_24_game(nodes)
    end = time.time()
    processing_time = (end-start) * 10**3
    if solutions:
        print("Here are the different solutions: ")
        #print(solutions[0])
        for solution in solutions:
            #solution.reverse()
            print(solution)
    else:
        print("No solutions found")
    print("Processing time: " + str(processing_time) + "ms")

main2()


"""def generate_start_nodes(graph,values,nodes):
    start_node = values
    new_values = []
    new_values = itertools.permutations(values)
    #graph = Graph(24,directed=True)
    for i in new_values:
        graph[i] = (tuple(start_node),tuple(i),"")
    return graph
    


def generateTree(node,graph):
    if len(node) > 1:
        for i in operations:
            new_node = list(node)
            action = i
            if i == "plus":
                a1 = node[0] + node[1]
            elif i == "minus":
                a1 = node[0] - node[1]
            elif i == "divide":
                a1 = node[0] / node[1]
            else:
                a1 = node[0] * node[1]
            new_node.pop(0)
            new_node.pop(0)
            new_node.insert(0,a1)
            add_node = tuple(new_node)
            graph[node] = (node,add_node,i)
            #nodes.append(add_node)
            generateTree(add_node,graph)
    else:
        graph[node]=(node,None,None)
        #nodes.append(node)

   
def generate_path(node, graph, start_node):
    current_node = start_node
    path = []
    for i in graph.keys():
        if i == current_node:
            for edge in i:
                if edge[0] == node and edge[1] != ():
                    path.append(edge)
                    new_node = edge[1]
                    current_node = new_node
    return path




def dfs(visited,graph, start_node,goal_node,path=[],operations=[]):
    path.append(start_node)
    visited.append(start_node)
    print("Start node: ", start_node)
    if start_node == goal_node:
        print(path)
        return path
        
    for node,edge in graph.items():
        if node == start_node:
            new_node = edge(1)
            if new_node not in visited:
                result = dfs(visited,graph,new_node,goal_node,path)
                if result is not None:
                    return result







def main():
    nodes = []
    graph = {}
    path = []
    paths = []
    
    graph = generate_start_nodes(graph,values,nodes)
    for i in nodes:
        generateTree(i,graph)
        
    #print(len(nodes))
    #for k,v in graph.items():
        #paths.append(dfs(path,graph,k))

    #print(node_test)
    goal_node = (24)
    visited = []
    
    print
    #print(graph(nodes[0]))
    #paths.append(dfs(visited,graph, nodes[0],goal_node,path))
    print(values)
    print(paths)
    
main()
"""